# https://www.codewars.com/kata/5b180e9fedaa564a7000009a
 
def solve(s):
    upper_count = sum(list(map(lambda x: 1 if x.isupper() and x.isalpha() else 0, s)))
    lower_count = sum(list(map(lambda x: 1 if x.islower() and x.isalpha() else 0, s)))
    s_clean = ''
    if upper_count > lower_count:
        s_clean = s.upper()
    elif lower_count > upper_count:
        s_clean = s.lower()
    else:
        s_clean = s.lower()
    
    return(s_clean)

