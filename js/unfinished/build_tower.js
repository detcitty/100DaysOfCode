// https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/javascript

/*
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.
*/
function towerBuilder(nFloors) {
  // build here
  // dealing with odd numbers
  var visual_floors = [];
  for (var i = i; i <= nFloors; i++) {
    visual_floors.push(2 * i * "*");
  }
  return visual_floors;
}
