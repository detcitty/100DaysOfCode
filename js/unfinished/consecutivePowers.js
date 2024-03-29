//https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/javascript

/*
The number 89 is the first integer with more than one digit that fulfills the 
property partially introduced in the title of this kata. What's the use of 
saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b 
that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers 
in the range that fulfills the property described above.

Let's see some cases (input -> output):

1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a, b] the function should 
output an empty list.

90, 100 --> []

Enjoy it!!
What to do?
*/

function sumDigPow(a, b) {
  // Your code here
  /*
  89 = 8^1  + 9^2
  */
  var split_nums = [];
  for (var i = a; i <= b; i++) {
    var nums = String(i)
      .split("")
      .map((str) => Number(str));
      split_nums.push(nums);
  }
  console.log(split_nums)

  for (var i = 0; i <= split_nums.length; i++) {
    const new_values = split_nums.map((str) => str**i);
    split_nums.push(new_values)
  }
  return split_nums;
}

const test1 = sumDigPow(1, 15)
console.log(test1)