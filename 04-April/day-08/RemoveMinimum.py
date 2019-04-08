# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

def remove_smallest(numbers):
    num = 0
    index = 0
    remove_numbers = []
    Found = False

    if(len(numbers) == 0):
        return(numbers)
    else:
        num = min(numbers)
            #print(num)
        for i in range(len(numbers)):
            if(numbers[i] == num and Found == False):
                Found = True
                continue
            remove_numbers.append(numbers[i])
        #print(numbers)
    return(remove_numbers)


remove_smallest([1, 2, 3, 4, 5])
