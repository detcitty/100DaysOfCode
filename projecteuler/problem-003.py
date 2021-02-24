import numpy as np

end_ = 600851475143
end_2 = 10
prime_numbers = []
for i in range(1, end_2):
    if (i <= 2 or i % 2 != 0):
        prime_numbers.append(i)
        for p in prime_numbers:
            if (i > 2 or i % p  == 0):
                prime_numbers.append(i)
            else:
                continue
    else:
        continue
    print(prime_numbers)

x = map(lambda x, y: x %y, np.arange(20), np.arange(20))
