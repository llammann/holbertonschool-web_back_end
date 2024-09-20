const http = require('http');

const port = 1245;
const host = 'localhost';

const app = http.createServer((request, response) => {
  res.statusCode = 200;
  res.end('Hello Holberton School!');
});

app.listen(port, host, () => {
  console.log(`Server listening at http://${hostname}:${port}`);
});

module.exports = app;
