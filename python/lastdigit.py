# https://www.codewars.com/kata/5f79b90c5acfd3003364a337/train/python

def last_digit(n):
	value = 1
	for i in range(n):
		value = value * i
	num_str = str(value)
	num_no_zeros = num_str.remove('0')
	lastdigit = num_no_zeros[-1]
    return(int(lastdigit))