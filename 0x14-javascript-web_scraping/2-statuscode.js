#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, resource, body) => {
  if (error) {
    console.log(`code: ${resource.statusCode}`);
    return;
  }
  console.log(`code: ${resource.statusCode}`);
});
