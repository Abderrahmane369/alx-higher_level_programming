#!/usr/bin/node
const request = require('request');

request(process.argv.splice(2)[0], (err, res, body) => {
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
