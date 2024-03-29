#!/usr/bin/node
// gets the contents of a webpage
// and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

request.get(url,
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      fs.writeFile(fileName, body, function (err) {
        if (err) console.error(err);
      });
    } else {
      console.error(error);
    }
  });
