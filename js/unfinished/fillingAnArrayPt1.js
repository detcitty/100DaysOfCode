//https://www.codewars.com/kata/571d42206414b103dc0006a1/train/javascript
/*

We want an array, but not just any old array, an array with contents!

Write a function that produces an array with the numbers 0 to N-1 in it.

For example, the following code will result in an array containing the numbers 0 to 4:

arr(5) // => [0,1,2,3,4]
Note: The parameter is optional. So you have to give it a default value.
*/
const arr = (N) => {
  var list1 = [];
  for (var i = 0; i < N; i++) {
    list1.push(i);
  }
  return list1;
};
