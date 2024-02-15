#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (ch) {
    if (ch === undefined) {
      ch = 'X';
    }
    let k = 0;
    for (k; k < this.height; k++) {
      console.log(ch.repeat(this.width));
    }
  }
}
module.exports = Square;
