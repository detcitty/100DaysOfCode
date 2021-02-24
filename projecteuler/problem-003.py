import numpy as np

end_ = 600851475143
end_2 = 10
prime_numbers = []
for i in range(1, end_2):
    print(prime_numbers)
    if (i > 2 or i % 2 != 0):
        for p in prime_numbers:
            if (i > 2 and i % p  == 0):
                print("PRIME NUM: {}".format(p))
                prime_numbers.append(i)
            else:
                print("HERE")
                break
    elif (i == 1 or i == 2):
        prime_numbers.append(i)
    else:
        print("OUTSIDE")
        continue
    print(prime_numbers)

x = map(lambda x, y: x %y, np.arange(20), np.arange(20))
