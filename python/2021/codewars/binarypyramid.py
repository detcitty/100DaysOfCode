# https://www.codewars.com/kata/5596700a386158e3aa000011/train/python

def binary_pyramid(m,n):
    #your code here
    all_numbers = []
    for i in range(m, n+1):
        numbers = []
        for x in [2**y for y in range(0, 5)]:
            if x > i:
                break
            elif (i % n == 0):
                numbers.append(1)
            
            else:
                numbers.append(0)

        all_numbers.append(numbers)
    print(all_numbers)
    sum_numbers = sum(all_numbers)

    return(all_numbers)

test1 = binary_pyramid(1,4)
print(test1)