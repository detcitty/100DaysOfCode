# https://www.codewars.com/kata/5f79b90c5acfd3003364a337/train/python

def last_digit(n):
    value = 1
    for i in range(1, n+1):
        value = value * i
    num_str = str(value)
    num_no_zeros = num_str.replace('0', '')
    lastdigit = list(num_no_zeros)[-1]
    return(int(lastdigit))

def last_digit_numpy(n):
    practice = np.arange(1, n+1)
    factorial = np.prod(practice)
    return(factorial)

print(last_digit(3))
print(last_digit_numpy(6))