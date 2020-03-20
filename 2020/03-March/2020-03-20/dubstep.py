# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
import re
def song_decoder(song):

    l = re.compile("(wub)", re.IGNORECASE).split(song)
    print(l)

    is_not_thing = lambda x: "wub" is not x
    cleaned_list = filter(is_not_thing, l)
    print(list(cleaned_list))
    return -1

song_decoder("AWUBWUBWUBBWUBWUBWUBC"),