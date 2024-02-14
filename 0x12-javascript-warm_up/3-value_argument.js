#!/usr/bin/node
const prc = require('process');
const ms_g = 'No argument';
if (prc.argv[2] === undefined) {
  console.log(ms_g);
} else {
  console.log(prc.argv[2]);
}
