#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let m = 0;
    for (m; m < this.height; m++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmpo = this.width;
    this.width = this.height;
    this.height = tmpo;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
