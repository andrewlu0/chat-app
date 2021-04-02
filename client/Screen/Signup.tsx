import React, { useContext, useRef, useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  Button,
  Alert,
  TouchableOpacity,
  TextInput,
} from "react-native";

import { AuthContext } from "../App"

interface Props {
  navigation: any;
}

const Signup = ({ navigation, ...props }: Props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [resp, setResp] = useState({ error: false, message: "" });
  const userInputRef = useRef(null);
  const passInputRef = useRef(null);
  var a = useContext(AuthContext);
  const handleSignup = async () => {
    var res = await a.Signup(username, password);
    setResp(res);
    if (!res.error){
      setUsername("");
      setPassword("");
    }
  };
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sign up</Text>
      <TextInput
        style={styles.inputStyle}
        onChangeText={(username) => setUsername(username)}
        placeholder="Enter username"
        autoCapitalize="none"
        blurOnSubmit={false}
        ref={userInputRef}
        value = {username}
      />
      <TextInput
        style={styles.inputStyle}
        onChangeText={(password) => setPassword(password)}
        placeholder="Enter password"
        autoCapitalize="none"
        blurOnSubmit={false}
        secureTextEntry={true}
        ref={passInputRef}
        value = {password}
      />
      <Text style={resp.error ? styles.error : styles.message}>
        {resp.message}
      </Text>
      <View style={styles.buttons}>
        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate("Home")}
        >
          <Text>Back</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={handleSignup}>
          <Text>Sign up</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default Signup;

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
  message: {
    color: "white",
    marginBottom: 20,
  },
});
