#!/usr/bin/node
// Write a script that prints x times “C is fun”

const myArray = 'C is fun';
const j = process.argv[2];
if (isNaN(j)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < j; i++) {
  console.log(myArray);
}
