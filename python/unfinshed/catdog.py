# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

'''
I'm not sure what is going on here
'''

def human_years_cat_years_dog_years(human_years):
    # Your code here
    cat = 0
    dog = 0

    '''
    for i in range(human_years):
        if i == 15:
            cat += 1
            dog += 1
        elif i == 24:
            cat += 1
            dog +=1
    '''

    if (human_years < 15):
        cat = 0
        dog = 0
    elif (human_years == 15):
        cat = 1
        dog = 1
    elif (human_years <= 24):
        cat = 2
        dog = 2
    else:
        cat = int(( human_years - (15 + 9) ) / 5)
        dog = int(( human_years - (15 + 9) ) / 4)
        

    return [human_years, cat, dog]
