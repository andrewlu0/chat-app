import React from "react";
import {
  StyleSheet,
} from "react-native";

// React Navigation
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

// Screens
import Home from "./Screen/Home";
import Login from "./Screen/Login";
import Signup from "./Screen/Signup";
import Chatroom from "./Screen/Chatroom";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerShown: false,
        }}
        initialRouteName="Chatroom"
      >
        <Stack.Screen
          name="Home"
          component={Home}
          options={{ title: "chat-app" }}
        />
        <Stack.Screen
          name="Login"
          component={Login}
          options={{ title: "login" }}
        />
        <Stack.Screen
          name="Signup"
          component={Signup}
          options={{ title: "sign up" }}
        />
        <Stack.Screen
          name="Chatroom"
          component={Chatroom}
          options={{ title: "Chatroom" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

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
    marginBottom: 20,
    borderRadius: 7,
  },
});
