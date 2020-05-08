#https://www.codewars.com/kata/5eb27d81077a7400171c6820/train/python

def graceful_tipping(bill):
    percent = bill * 0.15
    return(percent)

values = [1, 7, 12, 86, 99, 1149, 983212]

calc = list(map(graceful_tipping, values))
print(calc)