//https://www.codewars.com/kata/54da5a58ea159efa38000836/train/javascript

//https://stackoverflow.com/questions/1960473/get-all-unique-values-in-a-javascript-array-remove-duplicates
const onlyUnique = (value, index, self) => { return self.indexOf(value) === index };

function findOdd(A) {
  //happy coding!
  let unique_values = A.filter(onlyUnique);
  return(unique_values);
}
let test1 = findOdd([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]);

console.log(test1);