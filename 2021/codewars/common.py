import math

def convertFracts(lst):
	all_denoms = list(map(lambda x: x[1], lst))
	final_denom = math.prod(all_denoms)
	all_num = list(map(lambda x: ( final_denom * x[0] )/ x[1], lst))
	print(all_num)
	return(all_denoms)


val = convertFracts([[1, 2], [1, 3], [1, 4]])
print(val)