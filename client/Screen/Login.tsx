import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  Button,
  Alert,
  TouchableOpacity,
  TextInput,
} from "react-native";

import Authenticator from "../Authenticator";

interface Props {
  navigation: any;
}

const Login = ({ navigation, ...props }: Props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [resp, setResp] = useState({ message: "" });
  var a = new Authenticator();
  const handleLogin = async () => {
    var res = await a.Login(username, password);
    setResp(res);
    console.log(res);
    if (!res.error) {
      navigation.navigate("Chatroom", {
        username: username,
      });
    }
  };
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <TextInput
        style={styles.inputStyle}
        onChangeText={(username) => setUsername(username)}
        placeholder="Enter username"
        autoCapitalize="none"
        blurOnSubmit={false}
      />
      <TextInput
        style={styles.inputStyle}
        onChangeText={(password) => setPassword(password)}
        placeholder="Enter password"
        autoCapitalize="none"
        blurOnSubmit={false}
        secureTextEntry={true}
      />
      <Text style={styles.error}>{resp.message}</Text>
      <View style={styles.buttons}>
        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate("Home")}
        >
          <Text>Back</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={handleLogin}>
          <Text>Login</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default Login;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#13151a",
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    color: "white",
    fontSize: 30,
    padding: 20,
  },
  button: {
    alignItems: "center",
    backgroundColor: "#DDDDDD",
    padding: 10,
    marginRight: 20,
    borderRadius: 7,
  },
  buttons: {
    flexDirection: "row",
  },
  inputStyle: {
    marginBottom: 20,
    height: 40,
    padding: 10,
    backgroundColor: "#DDDDDD",
    borderRadius: 7,
  },
  error: {
    color: "red",
    marginBottom: 20,
  },
});
