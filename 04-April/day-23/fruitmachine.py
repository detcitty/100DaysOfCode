# https://www.codewars.com/kata/590adadea658017d90000039/train/python

from collections import Counter

def fruit(reels, spins):
    # Code here
    score = 0
    reel_length = len(reels)
    answers = []

    for i in range(3):
        if(reel_length != 1):
            answers.append(reels[i][spins[i]])
        else:
            answers.append(reel[spins[i]])
    count = Counter(answers)
    size_count = len(count.getkeys())
    if size_count == 3:
        score = 0
    return score




reel1 = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
reel3 = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
spin = [0,0,1]
print(fruit([reel1,reel2,reel3],spin))
