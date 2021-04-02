import React, { useContext, useEffect, useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  Button,
  Alert,
  TouchableOpacity,
  TextInput,
} from "react-native";
import { ScrollView } from "react-native-gesture-handler";

import { AuthContext } from "../App";

interface Props {
  route: any;
  navigation: any;
}

interface ChatProps {
  message: string;
  username: string;
  currentUser: string;
}

const Chatbox = ({ message, username, currentUser }: ChatProps) => {
  return (
    <>
      <View>
        <Text
          style={username === currentUser ? styles.myChat : styles.chatbox}
        >{`${username}: ${message}`}</Text>
      </View>
    </>
  );
};

const Chatroom = ({ route, navigation }: Props) => {
  var user = "";
  const [chat, setChat] = useState("");
  const [messages, setMessages] = useState([{ message: "", username: "" }]);
  var a = useContext(AuthContext);
  a.MessageStream().on("data", (chat) => {
    setMessages([...messages, chat]);
  });
  if (route.params) {
    const { username } = route.params;
    user = username;
  }
  const handleSubmit = () => {
    var msg = {
      message: chat,
      username: user,
    };
    a.SendChat(msg);
    // setMessages([...messages, msg])
    setChat("");
  };
  useEffect(() => {
    getChats();
  }, []);
  const getChats = async () => {
    var chats = await a.GetChats();
    setMessages(chats);
  };
  return (
    <>
      <View style={styles.header}>
        <Text style={styles.title}>Chatroom</Text>
        <TouchableOpacity
          style={styles.back}
          onPress={() => navigation.navigate("Home")}
        >
          <Text style={styles.back}>Back</Text>
        </TouchableOpacity>
      </View>
      <ScrollView>
        {messages.map((msg) => (
          <Chatbox
            message={msg.message}
            username={msg.username}
            currentUser={user}
          />
        ))}
      </ScrollView>
      <View style={styles.buttons}>
        <TextInput
          style={styles.inputStyle}
          onChangeText={(input) => setChat(input)}
          placeholder="Enter a message"
          autoCapitalize="none"
          blurOnSubmit={false}
          onSubmitEditing={handleSubmit}
          value={chat}
        />
        <TouchableOpacity style={styles.button} onPress={handleSubmit}>
          <Text>Send</Text>
        </TouchableOpacity>
      </View>
    </>
  );
};

export default Chatroom;

const styles = StyleSheet.create({
  header: {
    flexDirection: "row",
    backgroundColor: "#13151a",
    padding: 5,
    borderBottomWidth: 1,
    borderBottomColor: "white",
  },
  container: {
    overflow: "hidden",
  },
  title: {
    color: "white",
    backgroundColor: "#13151a",
    fontSize: 20,
    padding: 10,
  },
  button: {
    alignItems: "center",
    backgroundColor: "#DDDDDD",
    padding: 10,
    marginBottom: 20,
    borderRadius: 7,
    marginLeft: 10,
  },
  buttons: {
    flexDirection: "row",
    backgroundColor: "#13151a",
    paddingLeft: 40,
    paddingRight: 40,
  },
  inputStyle: {
    marginBottom: 20,
    height: 40,
    padding: 10,
    backgroundColor: "#DDDDDD",
    borderRadius: 7,
    flex: 1,
  },
  username: {
    backgroundColor: "#13151a",
    color: "white",
    padding: 10,
  },
  chatbox: {
    color: "white",
    fontSize: 18,
    backgroundColor: "#13151a",
    padding: 10,
    paddingLeft: 30,
  },
  myChat: {
    textAlign: "right",
    color: "white",
    fontSize: 18,
    backgroundColor: "#13151a",
    padding: 10,
    paddingRight: 30,
  },
  back: {
    marginLeft: "auto",
    padding: 5,
    backgroundColor: "#DDDDDD",
    borderRadius: 7,
  },
});
