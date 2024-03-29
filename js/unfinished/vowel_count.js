//https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript

/*
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
*/

function getCount(str) {
  //var vowelsCount = 0;
  const regexVowels = /[aeiou]/i;
  // enter your magic here
  let vowelsCount = [...str].filter(function (value) {
    return value.match(regexVowels);
  });
  return vowelsCount.length;
}
