// https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/javascript
/*
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

*/
function sumMix(x) {
  var s_new = x.map((x) => parseInt(x)).reduce((sum, number) => sum + number);
  return(s_new)
}
