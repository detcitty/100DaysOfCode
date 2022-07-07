# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

'''
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"
'''
def warn_the_sheep(queue):
    wolf_index = queue.index('wolf')
    