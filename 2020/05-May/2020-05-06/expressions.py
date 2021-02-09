# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python


def expression_matter(a, b, c):
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y
    first_add = add(a, b) + c
    second_add = a + add(b, c)

    add_multipy_first = multiply(a, b) + c
    add_multiply_second = a + multiply(b, c)

    multiply_one = multiply(a, multiply(b, c))
    multiply_second = multiply(multiply(a, b), c)

    

    values = [first_add, second_add, add_multipy_first, add_multiply_second, multiply_one, multiply_second]
    return(max(values))