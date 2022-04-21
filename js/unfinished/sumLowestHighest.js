// https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/javascript

function sumArray(array) {
    
  const sumWithInitial = array.reduce(
    (previousValue, currentValue) => previousValue + currentValue,
    0
  );
  return sumWithInitial - (Math.max(array) + Math.min(array));
}
