#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const array = process.argv.slice(1, process.argv.length);
if (array.length < 3) {
  console.log('0');
} else {
  const listString = array.map(Number);
  const list = listString.sort(function (a, b) { return b - a; })[2];
  console.log(list);
}
