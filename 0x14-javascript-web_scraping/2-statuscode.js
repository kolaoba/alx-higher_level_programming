#!/usr/bin/node
// displays the status code of a GET request.

const req = require('request');
const url = process.argv[2];

req.get(url,
		function (err, res, body) {
			code = res.statusCode;
			console.log(`code: ${code}`);
		}
);
