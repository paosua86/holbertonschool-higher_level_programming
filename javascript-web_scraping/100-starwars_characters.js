#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        console.log(JSON.parse(body).name);
      });
    }
  }
});
