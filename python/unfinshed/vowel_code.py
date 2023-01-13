# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

'''
Step 1: Create a function called encode() to replace all the lowercase vowels in
a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry
about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into
vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the
function wrrtg......;ill correspond to vowels.

'''
import regex as re


def encode(st):
    pattern = re.compile(r'[aeiou]', re.IGNORECASE)
    results = pattern.findall(st)


    vowel_dict = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    # [x for x in enumerate(vowel_dict)]
    for count, (k, v) in enumerate(vowel_dict.items()):
        re.sub(f"{v}")
    return


def decode(st):
    pattern = re.compile(r'[1-5]')
    results = pattern.findall(st)
    return
