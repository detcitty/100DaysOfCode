// https://www.codewars.com/kata/56606694ec01347ce800001b/train/javascript
/*
Implement a function that accepts 3 integer values a, b, c. The function should
 return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
*/
function isTriangle(a, b, c) {
  const perimeter = a + b + c;
  const s = 0.5 * perimeter;

  const squared_T = s * (s - a) * (s - b) * (s - c);
  const T = squared_T ** 0.5;
  return T;
}
