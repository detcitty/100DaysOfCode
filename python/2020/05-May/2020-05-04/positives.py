# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
    # Your code here

    numbers = list(map(lambda x: x > 0, arr))
    num_index = [i for i, x in enumerate(numbers) if x]
    values = list(map(lambda x, y: x if y else 0, arr, numbers))
    return(sum(values))

print(positive_sum([3,4,5,6]))