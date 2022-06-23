//https://www.codewars.com/kata/56530b444e831334c0000020/train/javascript

/*
Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.
*/
function chromosomeCheck(sperm) {
    var returnv = '';
    if (sperm = 'XY') {
        returnv = "Congratulations! You're going to have a son."
    }
    else {
        returnv = "Congratulations! You're going to have a daughter."

    }
    return(returnv)
}