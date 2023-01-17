#!/usr/bin/node
// prints the title of a Star Wars movie where
// the episode number matches a given integer.

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url,
  function (err, res, body) {
    if (err) console.error(err); else {
      const jsonBody = JSON.parse(body);
      console.log(jsonBody.title);
    }
  }
);
