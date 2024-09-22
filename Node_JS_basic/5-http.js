const http = require('http');
const processStudents = require('./3-read_file_async');

const serverPort = 1245;

const app = http
  .createServer(async (request, response) => {
    if (request.url === '/') {
      response.end('Welcome to Holberton School!');
    } else if (request.url === '/students') {
      response.write('Here is the list of our students\n');

      await processStudents(process.argv[2])
        .then((studentData) => {
          const fieldsArray = Object.keys(studentData);

          const totalCount = fieldsArray.reduce(
            (accumulator, currentField) => accumulator + studentData[currentField].totalCount,
            0,
          );

          response.write(`Total number of students: ${totalCount}\n`);

          for (let index = 0; index < fieldsArray.length; index += 1) {
            response.write(
              `Number of students in ${fieldsArray[index]}: ${studentData[fieldsArray[index]].totalCount}. `,
            );
            response.write(`List: ${studentData[fieldsArray[index]].namesList.join(', ')}`);

            if (index < fieldsArray.length - 1) {
              response.write('\n');
            }
          }
        })
        .catch((error) => {
          response.write(error.message);
        })
        .finally(() => {
          response.end();
        });
    }
  }).listen(serverPort);

module.exports = app;
