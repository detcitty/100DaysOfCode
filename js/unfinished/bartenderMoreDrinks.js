// https://www.codewars.com/kata/568dc014440f03b13900001d/train/javascript
/*
Complete the function that receives as input a string, and produces outputs according to the following table:
Input 	Output
"Jabroni" 	"Patron Tequila"
"School Counselor" 	"Anything with Alcohol"
"Programmer" 	"Hipster Craft Beer"
"Bike Gang Member" 	"Moonshine"
"Politician" 	"Your tax dollars"
"Rapper" 	"Cristal"
anything else 	"Beer"

Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer".

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, the input "pOLitiCIaN" should still return "Your tax dollars".

*/
function getDrinkByProfession(param) {
  const drinkTable = [
    ["Jabroni", "Patron Tequila"],
    ["School Counselor", "Anything with Alcohol"],
    ["Programmer", "Hipster Craft Beer"],
    ["Bike Gang Member", "Moonshine"],
    ["Politician", "Your tax dollars"],
    ["Rapper", "Cristal"],
  ];
  const r = drinkTable.filter(drink => drink[0] == param);

  if (r.length < 1 ) {
    return ("Beer");
  }
  else {
    return(r[1])
  }
}