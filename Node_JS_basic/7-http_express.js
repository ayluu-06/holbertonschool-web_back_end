const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      lines.shift();
      const counts = {};
      lines.forEach((line) => {
        const [firstname,, , field] = line.split(',');
        if (!counts[field]) counts[field] = [];
        counts[field].push(firstname);
      });
      const total = lines.length;
      resolve({ total, counts });
    });
  });
}

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');
  const dbFile = process.argv[2];
  try {
    const { total, counts } = await countStudents(dbFile);
    let response = 'This is the list of our students';
    response += `\nNumber of students: ${total}`;
    Object.entries(counts).forEach(([field, students]) => {
      response += `\nNumber of students in ${field}: ${students.length}. List: ${students.join(', ')}`;
    });
    res.send(response);
  } catch (err) {
    const errorResponse = `This is the list of our students\n${err.message}`;
    res.type('text/plain');
    res.send(errorResponse);
  }
});

if (require.main === module) {
  app.listen(port);
}

module.exports = app;
