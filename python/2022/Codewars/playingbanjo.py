## https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def are_you_playing_banjo(name):
    # Implement me!
    final_phrase = ''
    first_letter = name[0]
    if first_letter == 'R' or first_letter == 'r':
        final_phrase = "{} plays banjo".format(name)
    else:
        final_phrase = "{} does not play banjo".format(name)

    return final_phrase 