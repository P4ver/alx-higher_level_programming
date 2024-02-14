#!/usr/bin/node
const prc = require('process');
let nmb;
let mg = 'Not a number';
if (prc.argv.length > 2) {
  nmb = parseInt(prc.argv[2]);
  if (!isNaN(nmb)) {
    nmb = String(nmb);
    mg = `My number: ${nmb}`;
  }
}
console.log(mg);
