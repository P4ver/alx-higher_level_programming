#!/usr/bin/node
const prc = require('process');
const arv = prc.argv;
const arc = prc.argv.length;
if (arc < 4) {
  console.log(0);
} else {
  const arr = arv.slice(2).sort((a, b) => a - b).reverse();
  console.log(arr[1]);
}
