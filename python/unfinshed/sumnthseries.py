# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

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

    values = list(map(lambda n: 1/(1+n*3), range(0, n+1)))
    #This is a test
    
    return(sum(values))