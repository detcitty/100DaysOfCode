# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)

    if (distance_to_pump >= mpg * fuel_left):
    	return False
    else:
    	return True

print(zero_fuel(100, 50, 1))