# https://www.codewars.com/kata/52724507b149fa120600031d/train/python

def number2words(n):
    """ works for numbers between 0 and 999999 """
    map_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    numbers = list(map(lambda x: map_numbers[x], [int(i) for i in str(n)]))
    return(numbers)

test_ = number2words(1234)
print(test_)