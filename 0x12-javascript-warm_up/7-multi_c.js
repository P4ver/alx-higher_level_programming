#!/usr/bin/node
const prc = require('process');
let n_t = parseInt(prc.argv[2]);
const msg_1 = 'Missing number of occurrences';
const msg_2 = 'C is fun';
if (isNaN(n_t)) {
  console.log(msg_1);
} else {
  while (n_t > 0) {
    console.log(msg_2);
    n_t--;
  }
}
