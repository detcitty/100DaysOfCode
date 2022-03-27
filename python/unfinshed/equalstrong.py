# https://www.codewars.com/kata/5894017082b9fb62c50000df/train/python

def are_equally_strong(your_left, your_right, friends_left, friends_right):
  #coding and coding..

  return(True if (your_left == friends_left and your_right == friends_right) or (your_left == friends_right and your_right == friends_left) else False)