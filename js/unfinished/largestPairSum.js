//https://www.codewars.com/kata/556196a6091a7e7f58000018/train/javascript
/*
Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer.
*/
function largestPairSum(numbers) {
  //TODO: Write your Code here
  const first_max = Math.max(numbers);
  const first_index = numbers.indexOf(first_max);
  const removed_max = numbers.splice(first_index, 1); // 2nd parameter means remove one item only
  const second_max = Math.max(numbers);

  return [first_max, second_max];
}
