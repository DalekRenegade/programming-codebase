def findGameStatus(board):
    if not board:
        return "N"
    row_size = len(board)
    col_size = len(board[0])
    yellow_bitboard, red_bitboard = generateBitBoard(board, row_size, col_size)
    yellow_won = hasWon(yellow_bitboard, row_size, col_size)
    red_won = hasWon(red_bitboard, row_size, col_size)
    if yellow_won and red_won:
        return "B"
    if yellow_won:
        return "Y"
    if red_won:
        return "R"
    return "N"


"""
Function to generate bitboard for each player from the given matrix
Each cell is given a position as the bit position in a long number
An extra row is added at the top to handle the case of false positive when the hasWon uses bit shift
The bit board is represented for a 5x7 matrix as follows:


-  -  -  -  -  -  -
4 10 16 22 28 34 40
3  9 15 21 27 33 39
2  8 14 20 26 32 38
1  7 13 19 25 31 37
0  6 12 18 24 30 36

The top row represented by (-) is the buffer row. Thus, the bitboard contains (5+1)*7 = 42 bits (0-41 as
shown above).
If any index in the matrix is 'Y', the corresponding bit (as per the bit position in the above bitboard
representation)
of the player bitboard is set to 1. Others are 0.
"""


def generateBitBoard(board, row_size, col_size):
    yellow_bitboard, red_bitboard = 0, 0
    for j in range(col_size):
        for i in range(row_size - 1, -1, -1):
            bit = (j * row_size + j) + (row_size - i - 1)
            if board[i][j] == 'Y':
                yellow_bitboard |= (1 << bit)
            elif board[i][j] == 'R':
                red_bitboard |= (1 << bit)

    print "{0:b}".format(yellow_bitboard)
    print "{0:b}".format(red_bitboard)
    return yellow_bitboard, red_bitboard


"""
function to check if the player (represented by the bitboard) has won or not
Checks for all 4 direction. We shift each direction by 1 and perform bitwise AND.
The resultant 'temp' is again directionally (corresponding) shifted 2 more bits and bitwise ANDed with
'temp'
The final result will yeild if a particular sequence contains 1 or not.
Example:
consider a particular row represented by 01011110.
Its shifts are temp=(01011110 & 00101111)=00001110.
temp is now ANDed with 2 shifts of temp. So, (00001110 & 00000011) = 00000010
Thus a sequence of 4 or more 1s in the bitboard will boil down to 1 or 11 or 111 and so on.
Any sequence of less than 4 will be ANDed and the result will be 0.
The buffer row is used to remove the case of false positives which would occur when the bits are shifted
horizontally
and the top-most row of the matrix (i.e., 2nd row of the bitboard) is shifted and the bits overflow to the
next column which is undesirable.
"""


def hasWon(bitBoard, row_size, col_size):
    # horizontal
    m = bitBoard & (bitBoard >> (row_size + 1))
    if (m & (m >> (2 * (row_size + 1)))) >= 1:
        return True

    # vertical
    m = bitBoard & (bitBoard >> 1)
    if (m & (m >> 2)) >= 1:
        return True

    # diagonal 1
    m = bitBoard & (bitBoard >> row_size)
    if (m & (m >> (2 * row_size))) >= 1:
        return True

    # diagonal 2
    m = bitBoard & (bitBoard >> (row_size + 2))
    if (m & (m >> (2 * (row_size + 2)))) >= 1:
        return True

    return False


board = ["RRRR000","YYRYY00", "RRRYR0R", "YYYRRYR", "YRYRYYY", "RYRYRRR"]
print findGameStatus(board)
