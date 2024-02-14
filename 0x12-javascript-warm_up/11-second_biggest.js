#!/usr/bin/node
const prc = require('process');
const arg_v = prc.argv;
const arg_c = prc.argv.length;
if (arg_c < 4) {
  console.log(0);
} else {
  const arr = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(arr[1]);
}
