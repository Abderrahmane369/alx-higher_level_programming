#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2)[0];

request(`https://swapi-api.alx-tools.com/api/films/`, (err, res, body) => {
  if (err) console.log(err);

  const films = JSON.parse(body).results;
  const characters = films.map(val => {
    return val.characters;
  });
  const count = characters.map(val => {
    return val.filter(e => {
      return e.includes('18');
    });
  }).flat().length;

  console.log(count);
});
