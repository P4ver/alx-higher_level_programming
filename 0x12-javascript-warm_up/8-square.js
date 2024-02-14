#!/usr/bin/node
const prc = require('process');
const x = parseInt(prc.argv[2]);
const ms1 = 'Missing size';
if (isNaN(x)) {
  console.log(ms1);
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
