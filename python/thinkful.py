# https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python

def fillable(stock, merch, n):
    # Your code goes here.
    final_price = ''
    if merch in stock.keys():
    	available = merch[stock] 
    	if n >= available:
    		final_price = True
    	else:
    		final_price = False
    else:
    	final_price = False
    return(final_price)