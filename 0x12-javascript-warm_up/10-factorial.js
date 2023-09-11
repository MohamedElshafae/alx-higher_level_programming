#!/usr/bin/node

let fact = process.argv[2];

if (isNaN(fact)) {
  console.log(1);
} else {
  for (let index = fact - 1; index > 1; index--) {
    fact *= index;
  }
  console.log(fact);
}
