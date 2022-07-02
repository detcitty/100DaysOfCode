// https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/javascript
/*
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

*/
function factorial(n) {
  //your code here
  var total = 1;
  for (var i = n; i > 0; i--) {
    total = total * i;
  }
  return total;
}
