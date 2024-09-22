const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let dbInfo = 'This is the list of our students\n';

  try {
    const studentData = await countStudents(process.argv[2]);

    const totalStudents = studentData.total;
    const csStudents = studentData.locateCS || [];
    const sweStudents = studentData.locateSWE || [];

    dbInfo += `Number of students: ${totalStudents}\n`
              + `Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\n`
              + `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`;

    res.send(dbInfo);
  } catch (err) {
    dbInfo += err.message;
    res.status(500).send(dbInfo);
  }
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

module.exports = app;
