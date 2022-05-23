// https://www.codewars.com/kata/523f5d21c841566fde000009/train/javascript

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