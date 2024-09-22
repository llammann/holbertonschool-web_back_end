const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const reqUrl = url.parse(req.url, true);

  if (reqUrl.pathname === '/') {
    // When the URL path is '/'
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (reqUrl.pathname === '/students') {
    // When the URL path is '/students'
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    // Read and append student data from the database
    countStudents(process.argv[2])
      .then((studentsData) => {
        res.write(studentsData); // Write the student data to the response
        res.end(); // End the response after all data is written
      })
      .catch((err) => {
        res.write(err.message); // In case of error, write the error message
        res.end(); // End the response
      });
  } else {
    // For other paths
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

// The server should listen on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
