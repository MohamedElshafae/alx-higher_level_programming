#!/usr/bin/node

let i = 0;

process.argv.forEach((val) => {
  if (i > 1) {
    console.log(val);
  }
  i++;
});

if (i < 3) {
  console.log('No argument');
}
