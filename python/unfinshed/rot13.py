# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

'''
ROT13 is a simple letter substitution cipher that replaces 
a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string 
ciphered with Rot13. If there are numbers or special characters 
included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.


'''


def change_character(single_letter):
    char_number = ord(single_letter)
    final_value = None

    if (single_letter.islower()):
        # stuff
        final_value = ((char_number - ord('a') + 13) % 26) + ord('a')
    elif (single_letter.isupper()):
        # stuff
        final_value = ((char_number - ord('A') + 13) % 26) + ord('A')
    else:
        final_value = char_number
    return(chr(final_value))


def rot13(message):
    values = list(map(change_character, list(message)))
    #values = list(map(lambda x: chr(ord(x) + 13) + (chr(x) + 93) % 13, list(message)))
    #print(values)
    return(''.join(values))
