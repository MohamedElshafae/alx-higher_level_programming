#!/usr/bin/node
const Csquare = require('./5-square');

class Square extends Csquare {
	charPrint (c = 'X') {
		for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
			console.log(str);
    }
	}
}

module.exports = Square;
