# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python

def isPP(n):
	#your code here
	# Can I do a prime decomposition?
	odds = list(range(1, n+1, 2))
	potential_primes = list(map(lambda x: x**2, odds))

pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
