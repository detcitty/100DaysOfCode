import numpy as np
import time

values = []
for i in range(0, 10):
    values.append(i**i)

print(values)

print(time.strftime("%A", time.localtime()))

print(list(map(lambda x: 2**x, list(range(33)))))

sin_x = np.range(100)
print(np.numpy(sin_x))
