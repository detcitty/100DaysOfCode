# https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python
'''
Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. 
As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function that takes a pyramid representation as argument and returns its' largest 'slide down'. For example:
'''
import statistics
def longest_slide_down(pyramid):
    # TODO: write some code...
    
    # Should I make a class?
    avg = map(lambda x: statistics.mean(x), pyramid)
    ## What's the average of each row?
    
    pass

