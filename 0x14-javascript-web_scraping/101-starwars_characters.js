#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, resource, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const charactersUrl = JSON.parse(body).characters;
  charactersUrl.forEach(characterUrl => {
    request.get(characterUrl, (err, res, bd) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(bd).name);
    });
  });
});
