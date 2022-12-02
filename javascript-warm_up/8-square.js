#!/usr/bin/node
// Write a script that prints a square

const myArray = 'x';
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  console.log(myArray.repeat(size));
}
