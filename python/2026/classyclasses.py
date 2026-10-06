# https://www.codewars.com/kata/55a144eff5124e546400005a/train/python

class Person:
    def __init__(self, name_of_person, age_of_person):
        self.name = name_of_person
        self.age = age_of_person
        self.info = f"{self.name}s age is {self.age}"