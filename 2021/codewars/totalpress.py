# https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a/train/python

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # your code goes here
    m1 = molar_mass1 / given_mass1
    m2 = molar_mass2 / given_mass2

    R = 0.082
    
    p_total = ((m1 + m2) * (R * temp * 273.15) )/  volume
    return(p_total)