# https://www.codewars.com/kata/5913152be0b295cf99000001/train/python

def divisions(n, divisor):
    num = n
    count = 0
    while (num > 1):
        if (num % divisor == 0) :
            num = (num / divisor)
            count += 1
        else :
            num = 1
    return(count)

test1 = divisions(9999, 3)
print(test1)