# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
import re
def song_decoder(song):

    l = re.compile("wub", re.IGNORECASE).split(song)
    #print(l)

    is_not_thing = lambda x: x is not ""
    cleaned_list = filter(is_not_thing, l)
    value = ""
    for c in cleaned_list:
        value += c + " "
    #print(list(cleaned_list))
    return(value.strip())

print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))