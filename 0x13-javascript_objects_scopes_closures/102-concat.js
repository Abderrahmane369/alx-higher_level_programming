#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.splice(2);

const fileA = fs.readFileSync(argv[0], 'utf8');
const fileB = fs.readFileSync(argv[1], 'utf8');
fs.writeFile(argv[2], fileA + fileB, (err) => {
  if (err) throw err;
});
