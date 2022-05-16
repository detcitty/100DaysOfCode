// https://www.codewars.com/kata/5663f5305102699bad000056/train/javascript

function mxdiflg(a1, a2) {
  // your code
  var max_int = 0;
  if (a1.length == 0 || a2.length == 0) {
    max_int = -1;
  } else {
    for (var j = 0; j < a2.length; j++) {
      for (var i = 0; i < a1.length; i++) {
        var diff = Math.abs(a2[j].length - a1[i].length);
        max_int = diff > max_int ? diff : max_int;
      }
    }
  }
  return max_int;
}
