# https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python

def thirt(n):
    # your code
    remainders = [1, 10, 9, 12, 3, 4]
    sum = 0
    for i in map(int, str(n)):
        step = remainders[i % 6]
        sum += i * step
        print(step)

thirt(8529)
