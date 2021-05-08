# https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

def change(st):
    values = list(st.lower())
    how_ = list(map(lambda x: ord(x), values))
    unique_values = sorted(list(set(how_)))
    alpha = list(map(lambda x: chr(x), unique_values))
    print(alpha)
    only_alpha = list(filter(lambda x: x if x >=97 and x < 124 else "", unique_values))
    print(only_alpha)
    return(unique_values)

tst = change('!!a$%&RgTT')
print(tst)