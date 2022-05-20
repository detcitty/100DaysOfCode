//https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/javascript

function findNeedle(haystack) {
  // your code here
  var position = haystack.indexOf('needle') + 1;
  return(`found the needle at position ${position}`)
}