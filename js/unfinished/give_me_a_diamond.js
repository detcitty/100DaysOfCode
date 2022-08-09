// https://www.codewars.com/kata/5503013e34137eeeaa001648/train/javascript
/*
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a 
diamond string from James. Since James doesn't know how to make this happen, he needs your help.
Task

You need to return a string that looks like a diamond shape when printed on the screen, 
using asterisk (*) characters. Trailing spaces should be removed, and every line must 
be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not 
possible to print a diamond of even or negative size.
Examples

A size 3 diamond:

 *
***
 *

...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *

...that is:

"  *\n ***\n*****\n ***\n  *\n"


*/
function diamond(n) {
  var final_return_value = "";
  if (n % 2 == 0 || n < 0) {
    final_return_value = null;
  } else {
    var mid_str = "";
    for (var i = 1; i <= n; i += 2) {
      mid_str += "*".repeat(i) + "\n";
    }
    var reverse = mid_str.split("\n").reverse();
    reverse.shift();
    reverse.join("\n");
    final_return_value = mid_str + reverse + "\n";
  }
  return final_return_value;
}

/*

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

*/
