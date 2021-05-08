# https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python
import math

def convertFracts(lst):
	all_denoms = list(map(lambda x: x[1], lst))
	final_denom = math.prod(all_denoms)
	all_num = list(map(lambda x: ( final_denom * x[0] )/ x[1], lst))

	final_list = list(map(lambda x, y: [x, y], all_num, [final_denom] * len(lst)))
	print(all_num)
	return(final_list)


val = convertFracts([[1, 2], [1, 3], [1, 4]])
print(val)