# https://www.codewars.com/kata/573d498eb90ccf20a000002a/train/python

def decode(strng):
    #your code here
    orignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    shifted = [9, 8, 7, 6, 0, 4, 3, 2, 1, 5]
    combinded = dict(list(zip(orignal, shifted)))
    str_nums = list(strng)
    nums = list(map(lambda x: int(x), str_nums))
    print(nums)

print(decode('test'))