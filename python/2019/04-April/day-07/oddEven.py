def oddOrEven(arr):
    length = len(arr)
    number = 0
    value = ""
    if(length == 0):
        value = "even"

    for i in range(length):
        number += arr[i]

    if(number % 2 == 0):
        value = "even"
    else:
        value = "odd"
    return(value)


print(oddOrEven([0, 1, 2]))
