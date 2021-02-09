# https://www.codewars.com/kata/541c8630095125aba6000c00/train/c

def string_and_list(number):
    num_list = list(str(number))
    num_list = list(map(lambda x: int(x), num_list))
    return(number, num_list)

def digital_root(n):
    str_num, num_list = string_and_list(n)

    if len(num_list == 1):
        return(num_list[0])
    else:
        sum_num = sum(num_list)
        new_str = digital_root(str(sum_num))
        if (len(sum) == 1):
            return(value)
        new_new = ''.join(list(map(lambda x: str(x), num_list)))
        digital_root()
    print(num_list)

digital_root(454324)