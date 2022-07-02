# https://www.codewars.com/kata/5547929140907378f9000039/train/python

def shortcut( s ):
    # ...
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_letters = list(filter(lambda x: x not in vowels, list(s)))
    return(''.join(filtered_letters))
    
