#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2)[0];

request(`https://swapi-api.alx-tools.com/api/films/${argv}`, (err, res, body) => {
  if (err) console.log(err);

  console.log(JSON.parse(body).title);
});
