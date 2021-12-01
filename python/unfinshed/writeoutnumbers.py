# https://www.codewars.com/kata/52724507b149fa120600031d/train/python

def number2words(n):
    """ works for numbers between 0 and 999999 """
    numbers = {
        '0' : 'zero',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine'
    }

    numbers_list = list(map(lambda x : numbers[x], list(str(n))))
    #print(numbers_list)
    return(numbers_list)

test1 = number2words(1001)
print(test1)