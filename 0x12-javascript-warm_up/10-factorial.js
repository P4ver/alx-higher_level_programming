#!/usr/bin/node
function factorial (nb) {
  if ((isNaN(nb)) || (nb === 1)) {
    return 1;
  }
  return factorial(nb - 1) * nb;
}
console.log(factorial(parseInt(process.argv[2])));
