# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python

def update_light(current):
    # Your code here
    '''
    What does this do?
    '''
    final = ''

    if current == 'green':
        final = 'yellow'
    elif current == 'yellow':
        final = 'red'
    else:
        final = 'green'
    return(final)
