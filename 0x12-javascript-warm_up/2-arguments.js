#!/usr/bin/node
const prc = require('process');
let msg;
if (prc.argv.length === 3) {
  msg = 'Argument found';
} else if (prc.argv.length < 3) {
  msg = 'No argument';
} else {
  msg = 'Arguments found';
}
console.log(msg);
