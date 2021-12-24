# https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python

def fillable(stock, merch, n):
    # Your code goes here.
    '''
    I'm not sure what the code does.
    I think I will try to understand what is going on.

    But I think this is what happening:
    - check if the key is available.
    '''
    final_price = ''
    if merch in stock.keys():
        available = stock[merch] 
        if available >= n:
            final_price = True
        else:
            final_price = False
    else:
        final_price = False
    return(final_price)
