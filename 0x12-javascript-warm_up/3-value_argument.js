#!/usr/bin/node

const argv = process.argv;

if (argv.at(2)) {
  console.log(argv.at(-1));
} else {
  console.log('No arguments');
}
