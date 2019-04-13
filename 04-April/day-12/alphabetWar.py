def alphabet_war(fight):
    #your code here
    left_side = {('w': 4), ('p': 3), ('b': 2), ('s': 1)}
    right_side = {('m': 4), ('q': 3), ('d': 2), ('z': 1)}

    left_score = 0
    right_score = 0

    for s in fight:
        if (s in left_side.keys()):
            left_score += left_side[s]
        if (s in right_side.keys()):
            right_score += right_side[s]
        else:
            continue

    answer = ""

    if(left_score > right_score):
        answer = "Left side wins!"
    elif(left_score < right_score):
        ansewr = "Right side wins!"
    else:
        answer = "Let's fight again"
    return(answer)
