import React from "react";

const { useState } = React;

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [canLogin, setCanLogin] = useState(false);

  const handleLogin = async () => {
    console.log(username, password);
    await fetch(
      `http://127.0.0.1:8000/login_user/${username}?password=${password}`
    )
      .then((res) => {
        if (res.status === 200) return res.json();
      })
      .then((resJson) => {
        setCanLogin(resJson["isSuccess"]);
      });
  };

  return (
    <div>
      {canLogin === "true" ? "hai" : null}
      <input
        type="text"
        name="username"
        id="username"
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="text"
        name="password"
        id="password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={() => handleLogin()}>login</button>
    </div>
  );
};

export default Login;
