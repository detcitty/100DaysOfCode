# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    # Your code goes here
    letters = dict.fromkeys(set(text))

    for i in text:

        if(letters[i] == None):
            letters[i] = 1
        else:
            letters[i] += 1
        #print(letters[i])
    count = 0

    for val in letters.values():
        if(val > 1):
            count += 1

    return count
print(duplicate_count("indivisibility"))
print(duplicate_count("ABBA"))
