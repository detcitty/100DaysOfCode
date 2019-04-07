# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def bouncingBall(h, bounce, window):

    height = h
    count = 0
    if ((h > 0 and window < h) and (bounce > 0 and bounce < 1)):
        while (height > 0):
            count += 1
            height = height * bounce
            print(height)
        return count

    return -1

bouncingBall(3, 0.66, 1.5)
