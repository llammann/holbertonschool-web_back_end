const http = require('http');

const port = 1245;
const host = 'localhost';

const app = http.createServer((request, response) => {
  response.statusCode = 200;
  response.end('Hello Holberton School!');
});

app.listen(port, host, () => {
  console.log(`Server listening at http://${host}:${port}`);
});

module.exports = app;
