const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer(async (req, res) => {
  if (req.method === 'GET') {
    if (req.url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.write('This is the list of our students\n');

      try {
        const val = await countStudents(process.argv[2]);
        res.write(`Number of students: ${val.arr.length}\n`);
        res.write(`Number of students in CS: ${val.locateCS.length}. List: ${val.locateCS.join(', ')}\n`);
        res.write(`Number of students in SWE: ${val.locateSWE.length}. List: ${val.locateSWE.join(', ')}\n`);
      } catch (err) {
        res.write('This is the list of our students\n');
        res.end(err.message);
        return;
      }

      res.end();
    } else {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('Not Found');
    }
  } else {
    res.writeHead(405, { 'Content-Type': 'text/plain' });
    res.end('Method Not Allowed');
  }
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
