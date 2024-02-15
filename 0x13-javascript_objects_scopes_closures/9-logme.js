#!/usr/bin/node
let li = 0;
exports.logMe = function (item) {
  console.log(li + ': ' + item);
  li++;
};
