// https://www.codewars.com/kata/5899642f6e1b25935d000161/train/javascript
//import structuredClone from '@ungap/structured-clone';

/*
What are some of the issues to work on?
I want to format the code.
*/
function mergeArrays(arr1, arr2) {
    let array3 = arr1.concat(arr2);
    let deep_clone = structuredClone(array3)
    deep_clone.sort();
    return(deep_clone)
}