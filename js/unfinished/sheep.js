//https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/javascript

var countSheep = function (num){
  //your code here
  var text = '';
  for (let i = 1; i < num+1; i++) {
    text += `${i} sheep...`;
  }
  return(text);
};