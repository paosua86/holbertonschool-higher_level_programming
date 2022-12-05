#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const array = process.argv.slice(1, process.argv.length);
if (array.length < 1) {
    console.log(0);
  } else {
    const list_string = array.map(Number);
    const list = list_string.sort(function(a,b){return b-a})[2];
    console.log(list);
  }
