// https://www.codewars.com/kata/550498447451fbbd7600041c/train/javascript

function comp(array1, array2){
    //your code here
    var squared = array1.map(x => Math.pow(x, 2));
    squared.sort();
    var sqrt = array2.map(x => Math.sqrt(x));
    sqrt.sort();
    var is_same = true;
    for (var i = 0; i < array1.length; i++){
        if(squared[i] == array2[i]) {
            continue;
        } else {
            is_same = false;
        }
    }
    return(is_same)
  }