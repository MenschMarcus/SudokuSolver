#!/usr/bin/env python3

###############################################################################
# INPUT
###############################################################################

SIZE = 9
X = None

SUDOKU = [
    [X, 3, X, X, X, 8, 1, 6, X],
    [X, X, 5, 1, 0, 2, X, X, 9],
    [X, X, X, 7, X, 4, X, X, X],
    [X, X, X, X, 2, X, X, 1, 3],
    [X, X, 2, 9, X, 5, 6, 8, 7],
    [X, X, 7, X, X, 3, X, X, X],
    [X, 2, 6, 8, 7, X, X, 5, X],
    [X, 5, X, X, X, 9, X, X, X],
    [4, X, X, X, X, 6, X, X, X],
]


###############################################################################
# IMPORTS
###############################################################################

# Classes
from Number import Number
from Cell import Cell
from Row import Row
from Column import Column
from Square import Square

# Helpers
import sys
import math

###############################################################################
# FUNCTIONS
###############################################################################

def check_number(num):
    # error handling 1; ensure that Number is
    # - int between 0 and SIZE of Sudoko
    # - OR: None

    try:
        number = int(num)
        if number >= 0 and number <= SIZE:
            return number
        else:
            sys.exit("Error: number in Sudoku not in range")

    except:
        return None



###############################################################################
# MAIN
###############################################################################

# CREATE INITIAL STRUCTURES
# =========================

print("Hello World!")

# 1) Number
numbers = []
for i in range(0, SIZE+1):
    numbers.append(Number(i))
# special number: no number
no_number = Number(False)
numbers.append(no_number)

# 2) Cell -> Number
cells = []
for row in range(0, SIZE):
    cells_in_row = []
    for col in range(0, SIZE):
        # create cell with correct Number or None
        number = None
        cell_value = check_number(SUDOKU[row][col])
        if cell_value:
            cells_in_row.append(Cell(row, col, numbers[cell_value]))
        else:
            cells_in_row.append(Cell(row, col, no_number))
    cells.append(cells_in_row)

print(cells[3][4].number().value())

# 3.1) Row -> Cell -> Number
rows = []
for row_dx in range(0, SIZE):
    rows.append(Row(row_dx, cells[row_dx]))

# print(rows[3].column(4).number().value())

# 3.2) Column -> Cell -> Number
temp_columns = []
for col_dx in range(0, SIZE):
    temp_columns.append([])

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        temp_columns[col_idx].append(cells[row_idx][col_idx])

columns = []
for col_idx in range(0, SIZE):
    columns.append(Column(col_idx, temp_columns[col_idx]))
del temp_columns

# print(columns[3].row(4).number().value())

# 4) Square -> Cell -> Number
square_size = int(math.sqrt(SIZE))

# prepare structure: square[x][y]
squares = []
for square_row in range(0, square_size):
    squares.append([])
    for square_col in range(0, square_size):
        squares[square_row].append([])

# fill squares with inner sqauares
# os = outer square
# is = inner square
for os_row_idx in range(0, square_size):
    for os_col_idx in range(0, square_size):
        # for each square: prepare inner square (same size)
        inner_square = []
        for is_row in range(0, square_size):
            inner_square.append([])
            for is_col in range(0, square_size):
                inner_square[is_row].append([])
        # for each inner square: obtain inner square containing n cells
        for is_row_idx in range(0, square_size):
            for is_col_idx in range(0, square_size):
                cell = cells[os_row_idx*square_size + is_row_idx][os_col_idx*square_size + is_col_idx]
                inner_square[is_row_idx][is_col_idx] = cell
        # create new Square
        new_square = Square(os_row_idx, os_col_idx, inner_square)
        squares[os_row_idx][os_col_idx] = new_square

# print(squares[0][1].cell(1,2).number().value())

# CONNECT STRUCTURES
# ==================
