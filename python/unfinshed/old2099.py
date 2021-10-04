# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python

def calculate_age(year_of_birth, current_year):
    #your code here
    diff_year = current_year - year_of_birth

    if (diff_year > 1):
        return("You are {} years old.".format(diff_year))
    elif(diff_year == 1):
        return("You are 1 year old.")
    elif(diff_year == -1):
        return("You will be born in 1 year.")    
    elif(diff_year < -1):
        return("You will be born in {} years.".format(abs(diff_year)))
    else:
        return("You were born this very year!")
