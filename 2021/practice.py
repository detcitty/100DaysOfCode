import numpy
import time

values = []
for i in range(0, 10):
    values.append(i**i)

print(values)

print(time.strftime("%A", time.localtime()))
