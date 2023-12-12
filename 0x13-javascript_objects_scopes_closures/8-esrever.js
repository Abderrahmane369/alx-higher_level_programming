#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  for (const _ in list) arr[_] = list.at(-_);

  return arr;
};
