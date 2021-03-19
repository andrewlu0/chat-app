from concurrent import futures
import datetime
import time
import math
import logging
import psycopg2
from argon2 import PasswordHasher

import grpc

import auth_pb2
import auth_pb2_grpc

class AuthServicer(auth_pb2_grpc.AuthServicer):
    """Implements functionality of server
    """
    def __init__(self, db):
        self.db = db
        self.ph = PasswordHasher()

    def Signup(self, request, context):
        """Signs up user and returns error if username already exists.
        """
        try:
            cur = self.db.cursor()
            cur.execute("SELECT * FROM Users WHERE username='%s'" % request.username)
            user = cur.fetchone()
            if user is not None:
                cur.close()
                return auth_pb2.Response(error = True, message = "Username already exists.")
            hashed_pass = self.ph.hash(request.password)
            cur.execute("INSERT INTO Users VALUES ('%s', '%s')" % (request.username, hashed_pass))
            self.db.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return auth_pb2.Response(error = False, message = "Account created!")

    def Login(self, request, context):
        """Logs in user and returns error if username doesn't exist or password is incorrect.
        """
        try:
            cur = self.db.cursor()
            cur.execute("SELECT * FROM Users WHERE username='%s'" % request.username)
            user = cur.fetchone()
            cur.close()
            if not user:
              return auth_pb2.Response(error = True, message = "Username does not exist.")
            try:
                self.ph.verify(user[1], request.password)
            except (Exception):
                return auth_pb2.Response(error = True, message = "Incorret password.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return auth_pb2.Response(error = False, message = "Logged in!")
    
    def SendChat(self, request, context):
        """Sends chat to server
        """
        try:
            cur = self.db.cursor()
            cur.execute("INSERT INTO Messages (message, username, sent_at) VALUES ('%s', '%s', now())" %
                (request.message, request.username))
            self.db.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return auth_pb2.Response(error = False, message = "got chat")
    
    def GetChats(self, request, context):
        """Returns all chats in DB
        """
        try:
            cur = self.db.cursor()
            cur.execute("SELECT * FROM Messages")
            row = cur.fetchone()
            while row is not None:
              yield auth_pb2.Chat(message = row[1], username = row[2])
              row = cur.fetchone()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
          
def init_db():
    try:
        conn = psycopg2.connect(host="localhost",
                                  port ="5000",
                                  database="postgres",
                                  user="postgres",
                                  password="password")
        cur = conn.cursor()
        commands = (
          """
          CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
          """,
          """
          CREATE TABLE IF NOT EXISTS Users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL
          )
          """,
          """
          CREATE TABLE IF NOT EXISTS Messages (
            message_id uuid DEFAULT uuid_generate_v1 () ,
            message TEXT NOT NULL,
            username VARCHAR(255) NOT NULL,
            sent_at timestamp with time zone, 
            PRIMARY KEY (message_id),
            FOREIGN KEY (username) REFERENCES Users(username)
          )
          """
        )
        for command in commands:
          cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

def serve(db):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServicer_to_server(
        AuthServicer(db), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    db = init_db()
    serve(db)