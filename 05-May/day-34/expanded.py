# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
    size = len(str(num))
    str_num = str(num)
    #print(size, str_num)
    numbers = []
    for i, e in enumerate(str_num):
        #print(i, e)
        num_of_zeros = (size - i) - 1
        zeros = "0"* num_of_zeros
        combinded = e+zeros
        #print(combinded)

        if(int(combinded) != 0):
            numbers.append(combinded)

    final_str = ""
    s = 0
    while(s < len(numbers)):
        if (s == len(numbers) - 1):
            final_str += numbers[s]
        else:
            final_str += numbers[s] + " + "

        s += 1

    return(final_str)


expanded_form(70304)
