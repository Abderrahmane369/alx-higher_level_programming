#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4]));
console.log(esrever(['School', undefined, { id: 12 }, 'String']));
