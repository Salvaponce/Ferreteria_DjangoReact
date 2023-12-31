const Login = ({ handleLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('/api/login', {
      username,
      password,
    })
      .then((res) => {
        handleLogin(res.data.token);
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
            <h2>Iniciar sesión</h2>
            <Input
              type="text"
              name="username"
              placeholder="Nombre de usuario"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <Input
              type="password"
              name="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button type="submit">Iniciar sesión</Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};
