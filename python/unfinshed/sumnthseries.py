# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

'''
Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
'''

def series_sum(n):
    # Happy Coding ^_^
    '''
    1 --> 1
    2 --> 1 + 1/4 = 1 + 1/(2*2)
    3 --> 1 + 1/4 + 1/7 = 1 + 1/(2*2) + 1/7
    4 --> 1 + 1/4 + 1/7 + 1/10 = 1 + 1/(2*2) + 1/7 + 1/(2*5)
    5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 = 1 + 1/(2*2) + 1/7 + 1/(2*5) + 1/13 "1.57"
    f(n) --> 1 /(1+n*3)
    '''

    values = list(map(lambda n: 1/(1+n*3), range(0, n)))
    #This is a test
    #return(values)
    return("%.2f" % sum(values))

# print(series_sum(5))