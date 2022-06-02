// https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/javascript
/*
Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?
input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.

*/
function roundToNext5(n) {
  // ...
  var quotient = Math.floor(y / 5);
  var remainder = y % 5;
  return(quotient * 5 + 5);
}
