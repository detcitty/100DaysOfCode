# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):
    # Your code here
    cat = 0
    dog = 0
    for i in range(human_years):
        if i == 15:
            cat += 1
            dog += 1
        elif i == 24:
            cat += 1
            dog +=1

    return [human_years, cat, dog]
