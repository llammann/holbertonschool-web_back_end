const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const reqUrl = url.parse(req.url, true);

  if (reqUrl.pathname === '/') {

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (reqUrl.pathname === '/students') {

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');


    countStudents(process.argv[2])
      .then((studentsData) => {

        res.write(`${studentsData}\n`);
        res.end();
      })
      .catch((err) => {
        res.write(err.message);
        res.end();
      });
  } else {

    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});


app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
