import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import {
  Container,
  Row,
  Col,
  Button,
  Input,
  Form,
  Alert,
  Icon,
} from '@material-ui/core';
import {
  AccountCircle,
  Logout,
} from '@material-ui/icons';


const Register = ({ handleRegister }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('/api/register', {
      username,
      password,
      email,
    })
      .then((res) => {
        handleRegister(res.data.token);
      })
      .catch((err) => {
        console.error(err);
      });
  };

  return (
    <Container>
      <Row>
        <Col md={12}>
          <Form onSubmit={handleSubmit}>
            <h2>Sign up</h2>
            <Input
              type="text"
              name="username"
              placeholder="User name"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <Input
              type="password"
              name="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Input
              type="email"
              name="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)} />
              </Form>
              </Col>
              </Row>
              </Container>
              )
            }
