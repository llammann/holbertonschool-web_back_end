const http = require('http');
const countStudents = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const app = http.createServer(async (request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    let dbInfo = 'This is the list of our students\n';

    try {
      const message = await countStudents(process.argv[2]);
      dbInfo += message;
      response.end(dbInfo);
    } catch (err) {
      dbInfo += `Error: ${err.message}`;
      response.end(dbInfo);
    }
  } else {
    response.statusCode = 404;
    response.end('Not Found');
  }
});

app.listen(port, host, () => {
  console.log(`Server listening at http://${host}:${port}`);
});

module.exports = app;

