#!/usr/bin/node

const req = require('request');
const i_d = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const dt = JSON.parse(body);
  const d = dt.characters;
  for (const q of d) {
    req.get(q, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dt1 = JSON.parse(body1);
      console.log(dt1.name);
    });
  }
});
