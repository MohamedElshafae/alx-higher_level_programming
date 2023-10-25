#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, (error, resource, body) => {
  if (error) {
    console.error(error);
    return;
  }
  body = JSON.parse(body);
  const films = body.results;
  const numsMovies = countMoviesWithId(18, films);
  console.log(numsMovies);
});

function countMoviesWithId (charcterId, films) {
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes(characterId)) { count++; }
    }
  }
  return count;
}
