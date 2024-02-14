#!/usr/bin/node
const prc = require('process');
const x = parseInt(prc.argv[2]);
const msg_1 = 'Missing size';
if (isNaN(x)) {
  console.log(msg_1);
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
