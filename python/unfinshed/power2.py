# https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python

def powers_of_two(n):
    return list(map(lambda x: x^2, list(range(n))))

print(powers_of_two(5))
