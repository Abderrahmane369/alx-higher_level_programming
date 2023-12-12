#!/usr/bin/node

const arr = require('./100-data').list;

const maped = arr.map((e, i) => e * i);

console.log(arr);
console.log(maped);
