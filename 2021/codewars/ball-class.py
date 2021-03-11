# https://www.codewars.com/kata/53f0f358b9cb376eca001079/train/python

class Ball(object):
    def __init__(self, name=object):
        if name=="":
            self.ball_type = 'regulars'
        else:
            self.ball_type = object