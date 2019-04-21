# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
    # Code here
    words = x.split(" ")
    #print('a={:d}'.format(ord("a")))
    word_scores = []
    for w in words:
        score = 0
        for i in w:
            score += ord(i) - 96
        word_scores.append(score)
    #print(word_scores)
    value = word_scores.index(max(word_scores))

    return words[value]

print(high('man i need a taxi up to ubud'))
high('what time are we climbing up the volcano')
high("climbing")
high("volcano")
