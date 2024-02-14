#!/usr/bin/node
const prc = require('process');
const msg = 'No argument';
if (prc.argv[2] === undefined) {
  console.log(msg);
} else {
  console.log(prc.argv[2]);
}
