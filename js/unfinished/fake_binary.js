// https://www.codewars.com/kata/57eae65a4321032ce000002d/train/javascript
/*
Given a string of digits, you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
*/
function fakeBin(x){
    const myArray = x.split("");
    const finalValue = myArray.map( x => parseInt(x) * 2).join("");
    return(finalValue)
}