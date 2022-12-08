#!/usr/bin/node
// Write a script that display the status code of a GET request
const request = require('request');
const arg2 = process.argv[2];
request(arg2, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
