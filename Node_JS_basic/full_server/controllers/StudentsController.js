const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase('./path/to/database.csv');
      const students = data[major] || [];
      return res.status(200).send(`List: ${students.join(', ')}`);
    } catch (err) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
