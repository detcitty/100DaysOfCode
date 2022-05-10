// https://www.codewars.com/kata/568d0dd208ee69389d000016/train/javascript

function rentalCarCost(d) {
  // Your solution here
  var total_charges = 40 * d;
  var discount = 0;
  if (d >= 7) {
    discount = 50;
  }
  else if (d >= 3) {
    discount = 20;
  }
  else {
    discount = 0;
  }
  return(total_charges - discount)
}