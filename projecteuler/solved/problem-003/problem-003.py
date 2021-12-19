'''
i wish i was better at math problems 
i hipe i can solve

use a generator 
'''

import numpy as np

end_ = 600851475143
end_2 = 10
prime_numbers = []

print(prime_numbers)

half = end_ / 2
fake = np.arange(0, half, 2)
#print(fake)
for i in range(1, half):
    print(prime_numbers)

    if (i > 2 or i % 2 != 0):
        for p in prime_numbers:
            if (i > 2 and i % p  == 0):
                print("PRIME NUM: {}".format(p))
                prime_numbers.append(i)
            else:
                print("HERE")
                continue
    elif (i == 1 or i == 2):
        prime_numbers.append(i)
    else:
        print("OUTSIDE")
        break
    print(prime_numbers)

x = map(lambda x, y: x %y, np.arange(20), np.arange(20))
