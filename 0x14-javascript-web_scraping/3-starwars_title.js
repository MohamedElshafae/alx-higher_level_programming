#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, resource, body) => {
  if (error) {
    console.error(error);
    return;
  }
  body = JSON.parse(body);
  console.log(body.title);
});
