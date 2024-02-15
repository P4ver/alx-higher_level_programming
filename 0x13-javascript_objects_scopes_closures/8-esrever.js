#!/usr/bin/node
exports.esrever = function (list) {
  const revsList = [];

  for (let p = list.length - 1; p >= 0; p--) {
    revsList.push(list[p]);
  }
  return revsList;
};
