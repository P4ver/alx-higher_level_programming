#!/usr/bin/node
const prc = require('process');
let nmb;
let ms_g = 'Not a number';
if (prc.argv.length > 2) {
  nmb = parseInt(prc.argv[2]);
  if (!isNaN(nmb)) {
    nmb = String(nmb);
    ms_g = `My number: ${nmb}`;
  }
}
console.log(ms_g);
