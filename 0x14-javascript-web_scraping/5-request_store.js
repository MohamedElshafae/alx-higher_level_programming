#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = `${process.argv[2]}`;
const path = process.argv[3];

request.get(url, (error, resource, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(path, body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
