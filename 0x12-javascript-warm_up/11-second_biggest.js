#!/usr/bin/node

const argv = process.argv.splice(2);

function secondBiggest (arr) {
  if (arr.length === 0 || arr.length === 1) {
    return 0;
  }

  const a = arr;
  a.sort((a, b) => parseInt(b) - parseInt(a));

  return a[1];
}

console.log(secondBiggest(argv));
