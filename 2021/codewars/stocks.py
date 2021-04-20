# https://www.codewars.com/kata/597ef546ee48603f7a000057/train/python

def get_most_profit_from_stock_quotes(quotes):
    max_ = 0
    while (len(quotes) > 1):
        value = quotes.pop(0)
        next_value = quotes[1]

        max_ = max_ if max_ >= value else value
    return(max_)

