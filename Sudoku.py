X = None

SUDOKU_TEMPLATE = [
#    0  1  2    3  4  5    6  7  8

    [X, X, X,   X, X, X,   X, X, X],   # 0
    [X, X, X,   X, X, X,   X, X, X],   # 1
    [X, X, X,   X, X, X,   X, X, X],   # 2

    [X, X, X,   X, X, X,   X, X, X],   # 3
    [X, X, X,   X, X, X,   X, X, X],   # 4
    [X, X, X,   X, X, X,   X, X, X],   # 5

    [X, X, X,   X, X, X,   X, X, X],   # 6
    [X, X, X,   X, X, X,   X, X, X],   # 7
    [X, X, X,   X, X, X,   X, X, X],   # 8
]


SUDOKU_SIMPLE = [
#    0  1  2    3  4  5    6  7  8

    [3, 7, X,   X, 6, 2,   X, X, X],   # 0
    [X, 2, 9,   1, X, X,   7, X, X],   # 1
    [5, X, 1,   X, X, X,   9, 2, 8],   # 2

    [8, X, X,   4, 9, 6,   1, X, 7],   # 3
    [X, 4, X,   X, 1, X,   X, 9, 6],   # 4
    [1, X, 6,   7, 5, 3,   X, X, 4],   # 5

    [9, 8, 4,   X, X, X,   X, X, X],   # 6
    [X, X, X,   X, X, X,   X, 3, X],   # 7
    [6, 1, X,   X, 2, X,   5, 4, X],   # 8
]

SUDOKU_MEDIUM_SIMPLE = [
#    0  1  2    3  4  5    6  7  8

    [X, X, X,   8, X, 1,   3, 4, X],   # 0
    [3, X, 5,   X, 2, 6,   X, 7, 1],   # 1
    [X, X, X,   4, 7, X,   2, 5, X],   # 2

    [X, X, X,   X, X, X,   4, X, X],   # 3
    [X, 8, 7,   X, 4, X,   X, X, X],   # 4
    [2, 5, X,   X, X, 7,   6, 8, X],   # 5

    [X, X, 9,   X, X, 5,   1, X, 2],   # 6
    [X, 3, X,   X, X, X,   7, 6, 4],   # 7
    [X, X, 2,   7, X, X,   X, X, X],   # 8
]

SUDOKU_MEDIUM_HARD = [
#    0  1  2    3  4  5    6  7  8

    [X, X, X,   8, X, 1,   3, 4, X],   # 0
    [3, X, 5,   X, 2, 6,   X, 7, 1],   # 1
    [X, X, X,   4, 7, X,   2, 5, X],   # 2

    [X, X, X,   X, X, X,   4, X, X],   # 3
    [X, X, 7,   X, 4, X,   X, X, X],   # 4
    [2, 5, X,   X, X, 7,   6, 8, X],   # 5

    [X, X, 9,   X, X, 5,   1, X, 2],   # 6
    [X, 3, X,   X, X, X,   7, X, 4],   # 7
    [X, X, 2,   7, X, X,   X, X, X],   # 8
]

SUDOKU_HARD = [
#    0  1  2    3  4  5    6  7  8

    [X, 6, X,   1, 3, X,   X, 4, X],   # 0
    [X, X, X,   X, X, 8,   X, X, X],   # 1
    [9, 2, X,   7, X, X,   X, 5, 8],   # 2

    [3, 4, X,   2, X, X,   X, X, X],   # 3
    [X, X, 5,   X, X, 9,   X, X, 6],   # 4
    [X, 9, X,   X, X, 1,   X, X, 5],   # 5

    [X, X, X,   X, X, X,   1, 9, X],   # 6
    [X, 3, X,   9, X, X,   X, X, 7],   # 7
    [X, X, X,   X, 8, X,   X, X, X],   # 8
]

SUDOKU_EXPERT = [
#    0  1  2    3  4  5    6  7  8

    [X, X, X,   5, 2, X,   4, X, X],   # 0
    [X, X, X,   4, X, X,   X, X, 1],   # 1
    [X, X, X,   X, 8, X,   9, X, X],   # 2

    [X, 6, X,   X, X, X,   X, X, 4],   # 3
    [X, 7, X,   3, X, 2,   X, 8, 5],   # 4
    [X, 3, 8,   X, 7, X,   X, X, X],   # 5

    [9, X, X,   X, X, X,   X, X, X],   # 6
    [X, 5, X,   X, X, 3,   X, X, X],   # 7
    [X, X, 7,   1, X, X,   X, 4, 2],   # 8
]
