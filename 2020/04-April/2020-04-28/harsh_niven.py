# https://www.codewars.com/kata/54a0689443ab7271a90000c6/train/python

class Harshad:

    @staticmethod
    def is_value(number):
        var = list(str(number))
        back_to_int = lambda x: int(x)

        numbers = list(map(back_to_int, var))
        sum_num = sum(numbers)
        mod = number % sum_num
        return(mod == 0)

    @staticmethod
    def get_next(number):
        found = False
        n = number + 1
        while (found == False):
            check = Harshad.is_value(n)
            if (check):
                found = True
            else:
                n += 1
        return(n)


    @staticmethod
    def get_series(count, start=0):
        list_values = []
        found = 0
        num = start + 1 if start==0 else start
        while(found < count):

            is_harsh = Harshad.is_value(num)
            while(is_harsh == False):
                num = Harshad.get_next(num+1)
                is_harsh = True
            list_values.append(num)
            found += 1
        return(list_values)



print(Harshad.is_value(1001))
print(Harshad.get_next(17))
print(Harshad.get_series(3))