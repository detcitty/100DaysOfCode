// https://www.codewars.com/kata/57d814e4950d8489720008db/train/javascript

function index(array, n) {
  //your code here
  var return_value = 0;
  if (array.length < n ) {
    return_value = -1;
  } else {
    return_value = array[n] ** 2;
  }

  return return_value;
}
