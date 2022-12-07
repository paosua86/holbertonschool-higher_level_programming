#!/usr/bin/node
// Write a script that imports an array and computes a new array
const list = require('./100-data').list;
console.log(list);
const newList = list.map((value, index) => value * index);
console.log(newList);
