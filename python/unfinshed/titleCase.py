# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
'''

First argument (required): 
- the original string to be converted.
Second argument (optional): 
- space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

'''
def title_case(title, minor_words=''):
    title_list = title.split(' ')
    
    """
    my function
    :param value: value for my function; default is 1
    """
    if minor_words is title_case.__defaults__[0]:
        print('default')
        #minor_words = 'The'
    else:
        print('passed in the call')
    # whatever I want to do with the value
    print(minor_words)
    pass
    