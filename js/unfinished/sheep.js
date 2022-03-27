//https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/javascript

var countSheep = function (num){
  //your code here
  var text = '';
  for (let i = 0; i < num; i++) {
    text += `sheep ${i}`;
  }
  return(text);
};