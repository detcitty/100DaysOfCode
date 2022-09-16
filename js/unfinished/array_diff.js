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
    for (var i = 0; i < a.length; i++) {

        if (b.length > 0) {
            for (var j = 0; j < b.length; j++) {
                var left = a[i];
                var right = b[j];
                if (left != right) {
                    new_arr.push(left);
                } else {
                    continue;
                }
            }
        } else {
            b.forEach(x => new_arr.push(x));
        }
    }

    return (new_arr);
}