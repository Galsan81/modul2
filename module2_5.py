def get_matrix(n, m, value):
    matrix = []
    print(type(matrix))
    for i in range(n):
        for j in range(m):
            #matrix[i][j] = value
            matrix.append([value]*m)

    return matrix
print(get_matrix(2, 3, 7))