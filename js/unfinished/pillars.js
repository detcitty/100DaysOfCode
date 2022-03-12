// https://www.codewars.com/kata/5bb0c58f484fcd170700063d/train/javascript

function pillars(num_pill, dist, width) {
  // your code here
  var pills = dist * num_pill + width + (num_pill - 2);
  return(pills);
}