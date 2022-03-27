# https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

def add(num1, num2):
    num1_list = list(map(lambda x: int(x), list(str(num1))))
    num2_list = list(map(lambda x: int(x), list(str(num2))))
    print(num1_list)

    smallest_length = min(len(num1_list), len(num2_list))

    values = []

    for i in range(smallest_length):
        singleNum1 = num1_list[smallest_length-i-1]
        print(i, singleNum1)
        singleNum2 = num2_list[smallest_length-i-1]

        total = singleNum1 + singleNum2
        values.insert(0, total)

    if len(num1_list) > len(num2_list):
        pass
    elif len(num2_list) > len(num1_list):
        pass
    else:
        pass

    return(int(''.join(values)))

test1 = add(122,81)
print(test1)