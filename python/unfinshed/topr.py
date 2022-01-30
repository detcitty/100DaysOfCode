# https://www.codewars.com/kata/5838b5eb1adeb6b7220000f5/train/python

'''
A website named "All for Five", sells many products to registered clients that 
cost all the same (5 dollars, the price is not relevant). Every user receives an 
alphanumeric id code, like D085. The page tracks all the purchases, that the 
clients do. For each purchase of a certain client, his/her id user will be 
registered once.

You will be given an uncertain number of arrays that contains strings 
(the id code users). Each array will represent the purchases that the users 
do in a month. You should find the total number of purchases of the users 
that have bought in all the given months (the clients that their id code are 
present in all the arrays). e.g.:
'''

import pandas as pd

def id_best_users(*args):
    # your code here
    values = pd.read_data(args)
    return [[]]
