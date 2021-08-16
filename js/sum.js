// https://www.codewars.com/dashboard

// Sum Numbers
function sum (numbers) {
	var sum = 0;
	for(var i = 0; i < numbers.length; i++) {
		sum += numbers[i];
	}
	return(sum);
};

function sum(numbers) {
	numbers.forEach(x => {
		x.split(' ');
	});
};

var test1 = sum('1 2 3 4 5 6')
