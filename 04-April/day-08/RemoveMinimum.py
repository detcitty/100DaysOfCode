# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

def remove_smallest(numbers):
    num = min(numbers)
    index = Null
    for i in range(len(numbers)):
        if(numbers[i] == num):
            index = i
            break
    return(numbers.remove(index))        


remove_smallest([1, 2, 3, 4, 5])
