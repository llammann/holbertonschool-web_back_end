const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const port = 1245;
const app = express();

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');

  try {
    const data = await countStudents(database);
    const totalStudents = Object.values(data).reduce((acc, group) => acc + group.length, 0);
    res.write(`Number of students: ${totalStudents}\n`);

    for (const [field, group] of Object.entries(data)) {
      const names = group.map((student) => student.firstname).join(', ');
      res.write(`Number of students in ${field}: ${group.length}. List: ${names}`);
    }
    res.end();
  } catch (error) {
    res.end(`${error.message}`);
  }
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
