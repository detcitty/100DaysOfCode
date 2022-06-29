//https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/javascript

/*
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]

*/

function addLength(str) {
  //start-here
  const wordArray = str.split(" ");
  let wordSize = wordArray.map(function (elem) {
    return elem + " " + elem.length;
  });
  return(wordSize)
}
