#!/usr/bin/node

const numberOfTimes = process.argv[2];

if (isNaN(numberOfTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < numberOfTimes; index++) {
    console.log('C is fun');
  }
}
