#!/usr/bin/node
// displays the status code of a GET request.

const req = require('request');
const url = process.argv[2];

req.get(url,
  function (err, response, body) {
    if (err) console.error(err); else {
      const code = response.statusCode;
      console.log(`code: ${code}`);
    }
  }
);
