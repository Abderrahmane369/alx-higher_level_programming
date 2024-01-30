#!/usr/bin/node
const request = require('request');

request(process.argv.splice(2)[0], (err, res, body) => {
  if (err) console.log(err);

  let data = JSON.parse(body);
  let userTasks = {};

  data.forEach(element => {
    if (element.completed) {
      if (!userTasks[element.userId]) userTasks[element.userId] = 1;
      else {
        userTasks[element.userId]++;
      }
    }
  });

  console.log(userTasks);
});
