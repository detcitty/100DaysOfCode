# https://www.codewars.com/kata/52724507b149fa120600031d/train/python
'''
How can I make a machine learning algorithm?
'''
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


    number_placement = {
        0 : 'one',
        1 : 'ten',
        2 : 'hundred',
        3 : 'one thousand',
        4 : 'ten thousand',
        5 : 'hundred thousand'
    }
    numbers_with_placement = []
    for index, value in enumerate(numbers_list):
        joined = f'{value}:{number_placement[len(numbers_list)-index-1]}'
        numbers_with_placement.append(joined)
    
    return(numbers_with_placement)

test1 = number2words(10001)
print(test1)