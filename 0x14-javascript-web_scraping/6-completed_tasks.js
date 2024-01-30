#!/usr/bin/node
const request = require('request');

request(process.argv.splice(2)[0], (err, res, body) => {
  if (err) console.log(err);

  let data = JSON.parse(body);
  data = data.filter(e => {
    return e.completed;
  });

  const userTask = {};

  for (let i = 1; i <= 10; i++) {
    const tArrLen = data.filter(e => {
      return e.userId === i;
    }).length;

    userTask[i.toString()] = tArrLen;
  }

  console.log(userTask);
});
