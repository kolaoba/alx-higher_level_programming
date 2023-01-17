#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(
  url,
  function (err, res, body) {
    if (err) console.error(err);
    const movie = JSON.parse(body);
    const characters = movie.characters;
    characters.forEach(function (character, idx) {
      request.get(
        character,
        function (err, res, body) {
          if (err) console.error(err);
          const charDetails = JSON.parse(body);
          console.log(charDetails.name);
        });
    });
  });
