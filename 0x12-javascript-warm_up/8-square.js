#!/usr/bin/node

const numberOfTimes = process.argv[2];

if (isNaN(numberOfTimes)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < numberOfTimes; index++) {
		let x = '';
		for (let index = 0; index < numberOfTimes; index++) {
			x += 'X'
		}
		console.log(x);
  }
}
