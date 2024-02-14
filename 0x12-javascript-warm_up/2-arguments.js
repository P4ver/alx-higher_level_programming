#!/usr/bin/node
const prc = require('process');
let ms_g;
if (prc.argv.length === 3) {
  ms_g = 'Argument found';
} else if (prc.argv.length < 3) {
  ms_g = 'No argument';
} else {
  ms_g = 'Arguments found';
}
console.log(ms_g);
