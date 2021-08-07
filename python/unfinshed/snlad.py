# https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python

class SnakesLadders():

    def __init__(self):
        # Code Here
        w, h = 10, 10
        Matrix = [[0 for x in range(w)] for y in range(h)]
        self.board = Matrix

    def play(self, die1, die2):
        # Code Here
        self.die1 = die1
        self.die2 = die2
        