# https://www.codewars.com/kata/5432fd1c913a65b28f000342/solutions/python

def multiplication_table(row,col):
    # Good Luck!
    table = [[] for x in range(row)]
    for i in range(row):
        for j in range(col):
            value = (i+1) * (j+1)
            table[i].append(value)
            # table[j][i] = value

    return table

print(multiplication_table(2,2))
