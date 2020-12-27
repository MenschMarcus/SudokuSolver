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
from Helpers import *

# Helpers
import sys
import math


###############################################################################
# GLOBAL VARIABLES
###############################################################################

numbers = []
cells = []
rows = []
columns = []
squares = []


###############################################################################
# FUNCTIONS
###############################################################################

# ============================================================================
# check if number is correct correct Number object
# ============================================================================
def check_number(num):
    # error handling: ensure that Number is either
    # int between 0 and SIZE of Sudoko
    try:
        number = int(num)
        if number >= 0 and number <= SIZE:
            return number
        else:
            sys.exit("Error: number in Sudoku not in range")

    # OR: None
    except:
        return None


# ============================================================================
# return correct Number object
# ============================================================================
def get_number(num):
    # error handling: ensure that Number is either:
    # Number between 0 and SIZE of Sudoko
    if num >= 0 and num <= SIZE:
        return numbers[num]
    else:
        return no_number


# ============================================================================
# update cell number => update all dependencies
# ============================================================================
def update_cell(row_idx, col_idx, num, is_fix=False):

    number = get_number(num)
    cell = cells[row_idx][col_idx]
    row = rows[row_idx]
    column = columns[col_idx]
    square = squares[row_idx//helpers.get_square_size()][col_idx//helpers.get_square_size()]

    # Cell <-> Number
    cell.number(number)
    number.add_cell(cell)


###############################################################################
# MAIN
###############################################################################

helpers = Helpers(SIZE)


# CREATE INITIAL STRUCTURES
# =========================

# 1) Number
for i in range(0, SIZE+1):
    numbers.append(Number(i, SIZE))
# special number: no number
no_number = Number(False, SIZE)
numbers.append(no_number)

# 2) Cell -> Number
for row in range(0, SIZE):
    cells_in_row = []
    for col in range(0, SIZE):
        # create cell initially with no number(None)
        cells_in_row.append(Cell(no_number))
    cells.append(cells_in_row)

# 3.1) Row -> Cell -> Number
for row_dx in range(0, SIZE):
    rows.append(Row(row_dx, cells[row_dx]))

# 3.2) Column -> Cell -> Number
temp_columns = []

for col_dx in range(0, SIZE):
    temp_columns.append([])

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        temp_columns[col_idx].append(cells[row_idx][col_idx])

for col_idx in range(0, SIZE):
    columns.append(Column(col_idx, temp_columns[col_idx]))

del temp_columns

# 4) Square -> Cell -> Number

# prepare structure: square[x][y]
for square_row in range(0, helpers.get_square_size()):
    squares.append([])
    for square_col in range(0, helpers.get_square_size()):
        squares[square_row].append([])

# fill squares with inner sqauares
# os = outer square
# is = inner square
for os_row_idx in range(0, helpers.get_square_size()):
    for os_col_idx in range(0, helpers.get_square_size()):
        # for each square: prepare inner square (same size)
        inner_square = []
        for is_row in range(0, helpers.get_square_size()):
            inner_square.append([])
            for is_col in range(0, helpers.get_square_size()):
                inner_square[is_row].append([])
        # for each inner square: obtain inner square containing n cells
        for is_row_idx in range(0, helpers.get_square_size()):
            for is_col_idx in range(0, helpers.get_square_size()):
                cell = cells[os_row_idx*helpers.get_square_size() + is_row_idx][os_col_idx*helpers.get_square_size() + is_col_idx]
                inner_square[is_row_idx][is_col_idx] = cell
        # create new Square
        new_square = Square(os_row_idx, os_col_idx, inner_square)
        squares[os_row_idx][os_col_idx] = new_square


# CONNECT STRUCTURES
# ==================

# 1) Number -> Row / Column / Square


# FILL INITAL NUMBERS
# ===================

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        cell_value = check_number(SUDOKU[row_idx][col_idx])
        if cell_value:
            update_cell(row_idx, col_idx, cell_value, True)


# test prints
print(cells[3][4].number().value())
print(rows[3].column(4).number().value())
print(columns[3].row(4).number().value())
print(squares[0][1].cell(1,2).number().value())
