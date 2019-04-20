def multiplication_table(row,col):
    # Good Luck!
    table = [[] for x in range(row)]
    for i in range(col):
        for j in range(row):
            value = i * j
            table[i][j] = value

    return table

print(multiplication_table(2,2))
