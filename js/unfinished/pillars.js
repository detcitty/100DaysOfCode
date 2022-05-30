// https://www.codewars.com/kata/5bb0c58f484fcd170700063d/train/javascript

/*
There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:

number of pillars (≥ 1);
distance between pillars (10 - 30 meters);
width of the pillar (10 - 50 centimeters).
Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).
*/

function pillars(num_pill, dist, width) {
  // your code here
  var pills = 0;
  // Check for even number of pillars
  if (num_pill % 2 == 0) {
    pills = (width * num_pill) + (num_pill - 1) * dist;

  } else { //check for odd number of pillars
    pills = (width * num_pill) + (num_pill - 2) * dist;

  }
  return (pills);
}