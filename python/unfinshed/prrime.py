# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python

def prime_factors(n):
	start = 2
	reduced_value = n:
	values = []
	repeat = True
	while(reduced_value != 1):
		if reduced_value % start == 0 and repeat == True:
			reduced_value = reduced_value / float(start)
			values.append(values)
			repeat = True
		else if repeat == False:
			if reduced_value % start == 0:
				pass
			else:
				pass
		else if repeat ==  True and reduced_value % start != 0:
			pass
		else:
			pass
