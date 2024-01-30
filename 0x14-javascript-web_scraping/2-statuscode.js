#!/usr/bin/node
const request = require('request');

request(process.argv.splice(2)[0], (err, res, body) => {
  console.log(`code: ${res.statusCode}`);
});
