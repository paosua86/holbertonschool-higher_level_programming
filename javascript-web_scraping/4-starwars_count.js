#!/usr/bin/node
// Write a script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const { argv } = require('process');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    let times = 0;
    for (const result of obtained.results) {
      for (const char of result.characters) {
        if (char.includes('/18/')) {
          times++;
        }
      }
    }
    console.log(times);
  }
});
