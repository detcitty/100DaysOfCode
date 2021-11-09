# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    filter_new = []
    for e in birds:
        if e in geese:
            continue
        else:
            filter_new.append(e)
    return(filter_new)