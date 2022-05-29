// https://www.codewars.com/kata/5503013e34137eeeaa001648/train/javascript

function diamond(n) {
  var final_return_value = "";
  if (n % 2 == 0 || n < 0) {
    final_return_value = null;
  } else {
    for (var i = 1; i <= n; i += 2) {
      var str_value = "*".repeat(i) + "\n";
      var reverse = str_value.split("").reverse().join("");
    }
  }
  return final_return_value;
}
