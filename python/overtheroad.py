# https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python

def over_the_road(address, n):
	even_ = True if address % 2 == 0 else False

	if even_:
		odd_list = list(range(address-1, 2*n, 2))
		even_list = list(range(address, address-2*n, -2))
	else:
		odd_list = list(range(address, 2*n, 2))
		even_list = list(range(address+1, address-2*n, -2))