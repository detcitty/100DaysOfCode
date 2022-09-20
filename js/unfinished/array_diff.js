// https://www.codewars.com/kata/523f5d21c841566fde000009/train/javascript
/*
Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present 
in list b keeping their order.

arrayDiff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be 
removed from the other:

arrayDiff([1,2,2,2,3],[2]) == [1,3]
*/

function arrayDiff(a, b) {
    var new_arr = [];

    if (a.length != 0 || b.length != 0) {
        for (var i = 0; i < a.length; i++) {
            var left = a[i];
            const notfoundInB = !b.includes(left);
            const alreadyAdded = new_arr.includes(left);
            if (notfoundInB & !alreadyAdded) {
                new_arr.push(left);
            } else {
                continue;
            }
        }
    } else {
        new_arr = [];
    }
    var new_array_deepcopy = JSON.parse(JSON.stringify(new_arr));
    return (new_array_deepcopy);
}