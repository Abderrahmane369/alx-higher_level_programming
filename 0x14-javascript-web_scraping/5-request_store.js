#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv.splice(2);

request(argv[0], (err, res, body) => {
  if (err) console.log(err);
  fs.writeFile(argv[1], body, err => {
    if (err) console.log(err);
  });
});
