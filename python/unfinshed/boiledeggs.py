# https://www.codewars.com/kata/52b5247074ea613a09000164/train/python

'''
you can put at most 8 eggs into the pot at once
it takes 5 minutes to boil an egg
we assume, that the water is boiling all the time (no time to heat up)
for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it
'''
def cooking_time(eggs):
    number_pots = eggs // 8
    remainding_eggs = eggs % 8

    total_time = number_pots * 5
    time_leftover_eggs = 5 if remainding_eggs > 0 else 0
    return(total_time + time_leftover_eggs)