// https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/javascript

function sumFracts(l) {
    // your code
    let denom = l.map(x => x[1]);
    return(denom);
}
let test1 = sumFracts([
    [1, 2],
    [1, 3],
    [1, 4]
]);
console.log(test1);