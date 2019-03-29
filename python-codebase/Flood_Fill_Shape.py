def fillShape(matrix):
    if not matrix:
        return None
    row_size = len(matrix)
    col_size = len(matrix[0])
    print row_size, col_size
    matrix = floodFill(matrix, row_size / 2, col_size / 2)
    return matrix


def floodFill(matrix, r, c):
    row_size = len(matrix)
    col_size = len(matrix[0])
    if (r < 0 or r >= row_size or c < 0 or c >= col_size or matrix[r][c] == 1):
        return matrix
    matrix[r][c] = 1
    matrix = floodFill(matrix, r - 1, c)
    matrix = floodFill(matrix, r, c - 1)
    matrix = floodFill(matrix, r + 1, c)
    matrix = floodFill(matrix, r, c + 1)
    return matrix


matrix = [[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 1, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]]

fillShape(matrix)