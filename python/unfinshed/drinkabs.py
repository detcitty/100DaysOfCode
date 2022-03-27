# https://www.codewars.com/kata/56170e844da7c6f647000063/train/python

def people_with_age_drink(age):
    return_value = ''
    if (age < 14):
        return_value = 'drink toddy'
    elif(age < 18):
        return_value = 'drink coke'
    elif(age < 21):
        return_value = 'drink beer'
    else:
        return_value = 'drink whisky'
    return(return_value)

test1 = people_with_age_drink(24)
print(test1)