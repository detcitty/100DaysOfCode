# https://www.codewars.com/kata/58e230e5e24dde0996000070/train/python

'''
What was the name of the website to test math problems.

Project Euler
'''

def next_prime(n):
    # have fun ^.^
    potential_prime = n+1
    found_prime = False
    while (found_prime == False):
        all_indices = []
        for i in range(1, n+1):
            if n % i == 0:
                all_indices.append(i)
    return(all_indices)

test1 = next_prime(14)
print(test1)