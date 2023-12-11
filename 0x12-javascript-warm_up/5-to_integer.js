#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt('My number: ' + argv[2]));
}
