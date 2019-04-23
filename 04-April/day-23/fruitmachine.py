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


reel = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [0,0,0]
fruit([reel,reel,reel],spin)
