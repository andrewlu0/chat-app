import React from "react"
import { StyleSheet, Text, View, Button, Alert, TouchableOpacity } from 'react-native';

interface Props {
  navigation: any;
}

const Home = ({ navigation, ...props } : Props) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>chat-app</Text>
      <TouchableOpacity
        style = {styles.button}
        onPress={() => navigation.navigate('Signup')}
      >
        <Text>Sign up</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style = {styles.button}
        onPress={() => navigation.navigate('Login')}
      >
        <Text>Log In</Text>
      </TouchableOpacity>
    </View>
  )
}

export default Home;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#13151a',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    color: "white",
    fontSize: 30,
    padding: 20
  },
  button: {
    alignItems: "center",
    backgroundColor: "#DDDDDD",
    padding: 10,
    marginBottom: 20,
    borderRadius: 7,
  },
});