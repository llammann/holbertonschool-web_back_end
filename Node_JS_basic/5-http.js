const http = require('http');
const count = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const app = http.createServer(async (request, response) => {
  response.statusCode = 200;
  if (request.url === '/') {
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    let dbInfo = 'This is the list of our students\n';
    await count(process.argv[2])
      .then((message) => {
        dbInfo += message;
        response.end(dbInfo);
      })
      .catch((err) => {
        dbInfo += err.message;
        response.end(dbInfo);
      });
  }
});

app.listen(port, host, () => {
  console.log(`Server listening at http://${host}:${port}`);
});

module.exports = app;




