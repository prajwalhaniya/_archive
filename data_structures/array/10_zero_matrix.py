def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_columns = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    for col in zero_columns:
        for i in range(rows):
            matrix[i][col] = 0


matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

zero_matrix(matrix)
print(matrix)