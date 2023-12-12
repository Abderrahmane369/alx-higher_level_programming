#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  for (const i in list) arr.push(list.at(-i - 1));
  return arr;
};
