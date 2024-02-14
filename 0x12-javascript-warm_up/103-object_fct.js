#!/usr/bin/node
const mOjct = {
  type: 'object',
  value: 12
};
console.log(mOjct);
mOjct.incr = function () {
  this.value++;
};
mOjct.incr();
console.log(mOjct);
mOjct.incr();
console.log(mOjct);
mOjct.incr();
console.log(mOjct);
