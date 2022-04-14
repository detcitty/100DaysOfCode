//https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/javascript

String.prototype.toJadenCase = function () {
  //...
  var words = this.split(' ');
  words.map(element => element[0].toUpperCase + element.substring(1));
  words
}
