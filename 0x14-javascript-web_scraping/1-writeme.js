#!/usr/bin/node
// writes a string to a file.

const fs = require('fs');
const file = process.argv[2];
const input = process.argv[3];

fs.writeFile(file, input, 'utf-8', function (err, input) {
  if (err) throw err;
  console.log('added');
});
