def high(x):
    # Code here
    words = x.split(" ")
    #print('a={:d}'.format(ord("a")))
    word_scores = []
    for w in words:
        score = -96
        for i in w:
            score += ord(i)
        word_scores.append(score)

    value = word_scores.index(max(word_scores))

    return words[value]

print(high('man i need a taxi up to ubud'))
