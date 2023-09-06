import React, { useState } from 'react';
import axios from 'axios';

function Login() {
  const [loginData, setLoginData] = useState({ username: '', password: '' });
  const [registerData, setRegisterData] = useState({ username: '', password: '' });
  const [token, setToken] = useState(null);

  // Función para manejar el inicio de sesión
  const handleLogin = async () => {
    try {
      const response = await axios.post('/login/', loginData);
      const token = response.data.token; // Suponiendo que el servidor devuelve un token al autenticar
      setToken(token);
    } catch (error) {
      console.error('Error al iniciar sesión:', error);
    }
  };

  // Función para manejar el registro
  const handleRegister = async () => {
    try {
      const response = await axios.post('/register/', registerData);
      const token = response.data.token; // Suponiendo que el servidor devuelve un token al registrarse
      setToken(token);
    } catch (error) {
      console.error('Error al registrar:', error);
    }
  };

  // Función para cerrar sesión
  const handleLogout = () => {
    setToken(null);
  };

  return (
    <div>
      {token ? (
        <div>
          <p>Usuario autenticado</p>
          <button onClick={handleLogout}>Cerrar sesión</button>
        </div>
      ) : (
        <div>
          <h2>Iniciar sesión</h2>
          <input
            type="text"
            placeholder="Usuario"
            value={loginData.username}
            onChange={(e) => setLoginData({ ...loginData, username: e.target.value })}
          />
          <input
            type="password"
            placeholder="Contraseña"
            value={loginData.password}
            onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
          />
          <button onClick={handleLogin}>Iniciar sesión</button>
          <h2>Registrarse</h2>
          <input
            type="text"
            placeholder="Usuario"
            value={registerData.username}
            onChange={(e) => setRegisterData({ ...registerData, username: e.target.value })}
          />
          <input
            type="password"
            placeholder="Contraseña"
            value={registerData.password}
            onChange={(e) => setRegisterData({ ...registerData, password: e.target.value })}
          />
          <button onClick={handleRegister}>Registrarse</button>
        </div>
      )}
    </div>
  );
}

export default Login;
