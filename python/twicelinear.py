# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

def dbl_linear(n):
	values = [1]

	while(len(values) < n):
		y = 2 * values[-1] + 1
		z = 3 * values[-1] + 1 
		values.append(y)
		values.append(z)
	return(values)