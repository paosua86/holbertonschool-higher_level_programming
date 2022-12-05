#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const array = process.argv.slice(1, process.argv.length);
if (array.length < 1) {
    console.log(0);
  } else {
    var list_string = array.map(Number);
    const list = list_string.sort();
    console.log(list.reverse()[1]);
  }
