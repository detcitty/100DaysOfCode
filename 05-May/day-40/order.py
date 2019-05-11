# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
def sort_array(source_array):
    # Return a sorted array.
    even_indices = []
    values = []

    for i, num in enumerate(source_array):
        if(num % 2 == 0):
            even_indices.append(i)
        else:
            values.append(num)
    
    values.sort()
    final_values = []
    index = even_indices.pop(0)

    for j in range(len(source_array)):
        print(index)
        if (j == index):
            final_values.append(source_array[index])
            if(len(even_indices) == 0):
                continue
            else:
                index = even_indices.pop(0)
        else:
            final_values.append(values.pop(0))
    #print(even_indices)
    return final_values

print(sort_array([5, 3, 2, 8, 1, 4]))