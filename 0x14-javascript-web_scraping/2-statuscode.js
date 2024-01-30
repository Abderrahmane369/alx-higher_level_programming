#!/usr/bin/node
const request = require('request');

request(process.argv.splice(2)[0], (err, res, body) => {
  if (err) console.log(`code: ${res.statusCode}`);
  console.log(`code: ${res.statusCode}`);
});
