#!/usr/bin/node
function factorial (n_b) {
  if ((isNaN(n_b)) || (n_b === 1)) {
    return 1;
  }
  return factorial(n_b - 1) * n_b;
}
console.log(factorial(parseInt(process.argv[2])));
