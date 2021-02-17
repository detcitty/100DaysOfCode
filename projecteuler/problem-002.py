import numpy as np

max_value = 4000000

values_array = [1, 2]
current_number = values_array[-1]
while values_array[-1] + values_array[-2] < max_value:
    next_value = values_array[-1] + values_array[-2]

    is_greater = True if next_value > max_value else False
    if not is_greater:
        values_array.append(next_value)
    else:
        values_array.append(next_value)

print(sum(values_array))