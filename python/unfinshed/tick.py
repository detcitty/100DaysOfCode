# https://www.codewars.com/kata/587edac2bdf76ea23500011a/train/python

'''
How can I become better?
'''

def interpreter(tape):
    # Your code here
    values = tape.split()
    unique_values = set(values)

    found = {}

    for e in values:
        found[e] += 1

    return(found)


