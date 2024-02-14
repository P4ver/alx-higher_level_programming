#!/usr/bin/node
const prc = require('process');
let nt = parseInt(prc.argv[2]);
const msg1 = 'Missing number of occurrences';
const msg2 = 'C is fun';
if (isNaN(nt)) {
  console.log(msg1);
} else {
  while (nt > 0) {
    console.log(msg2);
    nt--;
  }
}
