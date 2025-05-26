const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err || !data.trim()) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      students.forEach((line) => {
        const studentData = line.split(',');
        const name = studentData[0];
        const field = studentData[studentData.length - 1];

        if (!fields[field]) fields[field] = [];
        fields[field].push(name);
      });

      const output = [];
      output.push(`Number of students: ${students.length}`);
      for (const [field, names] of Object.entries(fields)) {
        output.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve(output);
    });
  });
}

module.exports = countStudents;
