#!/usr/bin/node

const argv = process.argv;

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) return 1;

  return n * factorial(n - 1);
}

console.log(factorial(parseInt(argv[2])));
