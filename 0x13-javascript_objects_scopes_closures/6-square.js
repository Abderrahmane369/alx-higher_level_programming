#!/usr/bin/node

const Square = require('./6-rectangle');

class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) c = 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
