# https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python
'''
What does this even do? 
Should I write psudo-code for these more complicated ones
This is a test
'''
def balanced_num(number):
    is_odd = True if number % 2 == 1 else False
    middle = []
    if is_odd:
        middle.append(len(number) / 2)
    else:
        
        middle.append(len(number)/ 2)
        middle.append(len(number) / 2 - 1)
        middle.append("")

    return(middle)

test1 = balanced_num(53421)
print(test1)
