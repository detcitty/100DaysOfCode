// https://www.codewars.com/kata/5601409514fc93442500010b/train/javascript

function betterThanAverage(classPoints, yourPoints) {
  var class_size = classPoints.length;
  const initialValue = 0;
  const sumWithInitial = classPoints.reduce(
    (previousValue, currentValue) => previousValue + currentValue,
    initialValue
  );
  const class_average = sumWithInitial / class_size;
  return(yourPoints > class_average)
}
