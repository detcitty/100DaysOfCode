import numpy as np

end_ = 600851475143
end_2 = 10
add_array = []
for i in range(end_2):
    values = np.arange(0, i)
    round_ = values % i
    if i % 2 != 0:
        add_array.append(i)
    print(add_array)

x = map(lambda x, y: x %y, np.arange(20), np.arange(20))
