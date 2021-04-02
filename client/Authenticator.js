import grpc from "grpc";
import * as protoLoader from "@grpc/proto-loader";

const authProto = protoLoader.loadSync("../proto/auth.proto");
var auth = grpc.loadPackageDefinition(authProto).auth;
var client = new auth.Auth(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

class Authenticator {
  constructor() {
    this.call = client.Message();
  }
  Signup(username, password) {
    return new Promise((resolve, reject) => {
      var user = {
        username: username,
        password: password,
      };
      client.Signup(user, (err, resp) => {
        if (err) {
          reject(Error(err));
        } else {
          resolve(resp);
        }
      });
    });
  }
  Login(username, password) {
    return new Promise((resolve, reject) => {
      var user = {
        username: username,
        password: password,
      };
      client.Login(user, (err, resp) => {
        if (err) {
          reject(Error(err));
        } else {
          resolve(resp);
        }
      });
    });
  }
  GetChats() {
    return new Promise((resolve, reject) => {
      var call = client.GetChats();
      var chats = [];
      call.on("data", (chat) => {
        chats.push(chat);
      });
      call.on("error", () => {
        reject(Error(err));
      });
      call.on("end", () => {
        resolve(chats);
      });
    });
  }
  SendChat(msg) {
    this.call.write(msg);
  }
  MessageStream(){
    return this.call;
  }
}

export default Authenticator;
