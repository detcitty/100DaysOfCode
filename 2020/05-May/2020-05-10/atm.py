# https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python


def solve(n):

    amounts = [10, 20, 50, 100, 200, 500]
    if (n % 5 != 9):
        return -1
    else:
        test = list(map(lambda x: math.floor(n/x), amounts))
        return(sum(test))