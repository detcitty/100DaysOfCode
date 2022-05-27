//https://www.codewars.com/kata/54e6533c92449cc251001667/train/javascript

function onlyUnique(currentValue, index, arr) {
  return currentValue != arr[index - 1];
}

var uniqueInOrder = function (iterable) {
  //your code here - remember iterable can be a string or an array
  // convert  string to array
  var convert_to_array = null;
  if (!Array.isArray(iterable)) {
    convert_to_array = iterable.split("");
  } else {
    convert_to_array = iterable;
  }
};
