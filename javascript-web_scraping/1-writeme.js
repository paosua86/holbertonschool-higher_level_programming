#!/usr/bin/node
// Write a script that writes a string to a file.
const fs = require('fs');
const arg2 = process.argv[2];
const arg3 = process.argv[3];
fs.writeFile(arg2, arg3, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  }
});
