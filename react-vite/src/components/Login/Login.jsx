// src/components/Login.jsx
import React from 'react';
import './Login.css';

const Login = () => {
  const handleLogin = () => {
    window.location.href = '/api/linkedin/login';
  };

  return (
    <div>
      <h2>Login with LinkedIn</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
