import numpy as np

end_ = 600851475143
end_2 = 10
for i in range(end_2):
    values = np.arange(0, i)
    round_ = values % i
    print(round_)

x = map(lambda x, y: x %y, np.arange(20), 3)
