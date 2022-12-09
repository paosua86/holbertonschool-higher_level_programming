#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file
const request = require('request');
const { argv } = require('process');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(argv[3], body, 'utf-8', (error, data) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
