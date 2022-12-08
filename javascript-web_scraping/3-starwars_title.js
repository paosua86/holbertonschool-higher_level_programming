#!/usr/bin/node
// Write a script that prints the title of a Star Wars
// movie where the episode number matches a given integer
const request = require('request');
const arg2 = process.argv[2];
const url = 'http://swapi.co/api/films/' + arg2;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});
