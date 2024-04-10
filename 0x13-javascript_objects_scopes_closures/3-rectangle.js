#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print() {
    let i = this.width; // Declare i using let
    let j = this.height; // Declare j using let
    while (i > 0) {
      while (j > 0) {
        console.log('X');
        j = j - 1;
      }
      console.log('\n'); // Use \n for newline
      i = i - 1;
    }
  }
}

module.exports = Rectangle;
