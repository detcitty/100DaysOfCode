// https://www.codewars.com/kata/5503013e34137eeeaa001648/train/javascript

function diamond(n) {
  var str_value = '';
  if (n % 2 == 0 || n < 0) {
    str_value = null;
  } else {

      for (var i = 1; i <= n ; i+=2) {
          str_value += '*'.repeat(i) +'\n'; 
      }
  }
  return str_value;
}
