# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python
'''
Description:

We want to generate a function that computes the series starting from 0 and ending until the given number.
Example:

Input:
> 6
Output:
    0+1+2+3+4+5+6 = 21
Input:
> -15
Output:
    -15<0
Input:
> 0
Output:
    0=0
'''


def show_sequence(n):
    if n > 0:
        numbers = list(range(0, n+1))
        total_sum = sum(numbers)
        string_value = "+".join(str(v)
                                for v in numbers) + " = " + str(total_sum)
        return(string_value)
    elif n == 0:
        return("0=0")
    else:
        return(f"{str(n)}<0")
