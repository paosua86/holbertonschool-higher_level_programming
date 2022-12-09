#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id
const request = require('request');
const { argv } = require('process');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const users = {};
    data.forEach(function (task) {
      if (task.completed) {
        if (users[task.userId]) {
          users[task.userId]++;
        } else {
          users[task.userId] = 1;
        }
      }
    });
    console.log(users);
  }
});
