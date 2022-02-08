# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python

def rps(p1, p2):
    #your code here
    return_value = ''
    if p1 == p2:
        return_value = 'Draw!'
    elif p1 == 'scissors' and p2 == 'paper':
        return_value = 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'rock':
        return_value = 'Player 2 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        return_value = 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'paper':
        return_value = 'Player 2 won!'
    elif p1 == 'paper' and p2 == 'scissors':
        return_value = 'Player 2 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return_value = 'Player 1 won!'
    return(return_value)
        