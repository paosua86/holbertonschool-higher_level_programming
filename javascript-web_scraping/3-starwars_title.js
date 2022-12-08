#!/usr/bin/node
// Write a script that prints the title of a Star Wars
// movie where the episode number matches a given integer
const request = require('request');
const { argv } = require('process');
const url = `https://swapi-api.hbtn.io/api/films/${argv[2]}`

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    console.log(`${obtained.title}`);
  }
});
