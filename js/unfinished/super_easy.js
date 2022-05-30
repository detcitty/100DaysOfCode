// https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/javascript

function problem(x) {
    //your code here
    return ((typeof x === 'string' || x instanceof String) ? "Error" : (x * 50 + 6));
}