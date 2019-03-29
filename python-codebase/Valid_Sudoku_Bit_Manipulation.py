def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    sub_grid_bits, row_wise_bits, col_wise_bits = [0] * 9, [0] * 9, [0] * 9
    i, j = 0, 0
    while i < 9:
        j = 0
        while j < 9:
            sub_grid_index = (i / 3) * 3 + j / 3
            if board[i][j] != '.':
                board_val = int(board[i][j]) - 1
                bits_val = sub_grid_bits[sub_grid_index]
                if (bits_val >> board_val) & 1 == 1:
                    return False
                sub_grid_bits[sub_grid_index] |= (1 << board_val)
                bits_val = row_wise_bits[i]
                if (bits_val >> board_val) & 1 == 1:
                    return False
                row_wise_bits[i] |= (1 << board_val)
                bits_val = col_wise_bits[j]
                if (bits_val >> board_val) & 1 == 1:
                    return False
                col_wise_bits[j] |= (1 << board_val)
            j += 1
        i += 1
    for v in sub_grid_bits:
        print format((v), '09b'),
    print ''
    return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
board2 = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]]

print isValidSudoku(board1)
print isValidSudoku(board2)
