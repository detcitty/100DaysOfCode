#https://www.codewars.com/kata/5eb27d81077a7400171c6820/train/python
import math

def graceful_tipping(bill):
    percent = bill * 0.15
    total = bill + percent

    if (total < 10):
        total += 1
        total = math.floor(total)
    elif (total >= 10 and total < 100):
        remainder = total % 5
        add_to_total = 5 - remainder
        total += add_to_total
        pass
    elif (total >= 10 and total < 100):
        remainder = total % 50
        add_to_total = 50 - remainder
        print(add_to_total)
        add_to_total_new = 50 if add_to_total==0 else add_to_total
        total += add_to_total_new
    else:
        remainder = total % 500
        add_to_total = 500 - remainder        
        print(add_to_total)
        add_to_total_new = 500 if add_to_total==0 else add_to_total
        total += add_to_total_new

    return(total)

values = [1, 7, 12, 86, 99,500, 1149, 983212]

calc = list(map(graceful_tipping, values))
print(calc)