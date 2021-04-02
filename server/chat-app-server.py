from concurrent import futures
import datetime
import time
import math
import logging
import threading


from argon2 import PasswordHasher
from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship
from uuid import uuid4

import grpc

import auth_pb2
import auth_pb2_grpc

base = declarative_base()
message_queue = []
update_chat = threading.Condition()

class User(base):
    __tablename__ = "users"
    username = Column(String, primary_key=True)
    password = Column(String)
    children = relationship("Chat")

class Chat(base):
    __tablename__="messages"
    message_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    text = Column(String)
    username = Column(String, ForeignKey("users.username"))
    timestamp = Column(Time)


class AuthServicer(auth_pb2_grpc.AuthServicer):
    """Implements functionality of server
    """
    def __init__(self, db):
        self.db = db
        self.ph = PasswordHasher()

    def Signup(self, request, context):
        """Signs up user and returns error if username already exists.
        """
        user_exist = self.db.query(User).filter_by(username=request.username).first()
        if user_exist:
            return auth_pb2.Response(error = True, message = "Username already exists.")

        hashed_pass = self.ph.hash(request.password)
        user = User(username = request.username, password = hashed_pass)
        self.db.add(user)
        self.db.commit()
        return auth_pb2.Response(error = False, message = "Account created!")

    def Login(self, request, context):
        """Logs in user and returns error if username doesn't exist or password is incorrect.
        """
        user = self.db.query(User).filter_by(username=request.username).first()
        if not user:
            return auth_pb2.Response(error = True, message = "Username does not exist.")
        try:
            self.ph.verify(user.password, request.password)
        except (Exception):
            return auth_pb2.Response(error = True, message = "Incorret password.")
        return auth_pb2.Response(error = False, message = "Logged in!")
    
    def Message(self, request_iterator, context):
        """Bidirectional stream of chat messages
        """
        q_size = len(message_queue)
        def receive():
            for msg in request_iterator:
                message_queue.append(msg)
                self.db.add(Chat(text= msg.message, username = msg.username, timestamp = datetime.datetime.now()))
                self.db.commit()
                with update_chat:
                    update_chat.notify_all()
        threading.Thread(target = receive).start()
        while True:
            with update_chat:
                update_chat.wait_for(lambda: len(message_queue) > q_size)
                yield message_queue[q_size]
                q_size += 1
                
    
    
    def GetChats(self, request, context):
        """Returns all chats in DB
        """
        chats = self.db.query(Chat)
        for chat in chats:
            yield auth_pb2.Chat(message = chat.text, username = chat.username)
          
def init_db():
    db = create_engine("postgresql://postgres:password@localhost:5000/postgres")
    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)
    return session

def serve(db):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServicer_to_server(
        AuthServicer(db), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    db = init_db()
    serve(db)