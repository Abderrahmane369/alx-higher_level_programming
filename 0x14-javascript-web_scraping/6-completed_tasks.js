#!/usr/bin/node
const request = require('request');

request(process.argv.splice(2)[0], (err, res, body) => {
  if (err) console.log(err);

  let data = JSON.parse(body);
  let userTasks = {};

  data.forEach(task => {
    if (task.completed && !userTasks[task.userId]) {
      userTasks[task.userId] = 1;
    } else if (task.completed) {
      userTasks[task.userId]++;
    }
  });

  console.log(userTasks);
});
