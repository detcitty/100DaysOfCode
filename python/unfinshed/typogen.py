# https://www.codewars.com/kata/55953e906851cf2441000032/train/python
import re

def scramble_words(words):
    #your code here
    words_list = words.split(r"\s+")
    new_string = ""

    for w in words_list:
        word_indices = list(range(len(w)))
        found_indices = []

        for i, chars in enumerate(w):
            alpha_regex = re.compile(r"[a-zA-Z]", flags=re.I)
            found_indices.append(i if i not in [0, len(w)-1] or alpha_regex.search(chars) else "")

        clean_indices = list(filter(None, found_indices))
        relevant_char = sorted(list(map(lambda word_str, idx: word_str[idx], w, clean_indices)))

        word_assembled = ""
        for j in found_indices:
            pass
    
    return(new_string)

test_ = scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.")

print(scramble_words)