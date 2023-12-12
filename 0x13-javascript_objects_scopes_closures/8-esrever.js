#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  for (const i in list) arr[i] = list.at(-i - 1);
  return arr;
};
