def convertFracts(lst):
	all_denoms = list(map(lambda x: x[1], list))
	return(all_denoms)

val = convertFracts([1, 2], [1, 3], [1, 4])
print(val)