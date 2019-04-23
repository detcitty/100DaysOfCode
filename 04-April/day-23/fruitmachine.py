def fruit(reels, spins):
    # Code here

    reel_length = len(reels)
    answers = []

    for i in range(3):
        if(reel_length != 1):
            answers.append(reels[i][spins[i]])
        else:
            answers.append(reel[spins[i]])

    return answers


reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
reel3 = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
spin = [5,4,3]
print(fruit([reel1,reel2,reel3],spin))
