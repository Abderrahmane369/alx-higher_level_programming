#!/usr/bin/node
const request = require('request');
const argv = process.argv.splice(2);

request(`https://swapi-api.alx-tools.com/api/films/${argv[0]}/`, (err, res, body) => {
  if (err) console.log(err);

  const characters = JSON.parse(body).characters;

  characters.forEach(element => {
    request(element, (err, res, body) => {
      if (err) console.log(err);

      console.log(JSON.parse(body).name);
    });
  });
});
