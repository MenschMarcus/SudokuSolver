#!/usr/bin/env python3

###############################################################################
# IMPORTS
###############################################################################

# Classes
from Sudoku import *
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

SIZE = 9

numbers = []
cells = []
rows = []
columns = []
squares = []

num_fixed_cells = 0


###############################################################################
# FUNCTIONS
###############################################################################

helpers = Helpers(SIZE)

# ============================================================================
# return correct Number object
# ============================================================================
def get_number(num):
    # error handling: ensure that Number is either:
    # Number between 1 and SIZE of Sudoko
    num = helpers.check_number(num)

    # NB: there is no 0 in Sudoku! => idx = value-1
    if num:
        return numbers[num-1]
    else:
        return no_number


# ============================================================================
# update cell number => update all dependencies
# ============================================================================
def update_cell(cell, number):
    # Cell <-> Number
    # => Row / Column / Square updates automatically
    cell.number(number)
    number.add_cell(row_idx, col_idx, cell)


# ============================================================================
# update cell number => update all dependencies
# ============================================================================
def print_sudoku():
    print("=========================")
    print("FINAL SUDOKU")
    for row_idx in range(0, SIZE):
        nums_in_row = []
        for col_idx in range(0, SIZE):
            num = cells[row_idx][col_idx].number().value()
            if num:
                nums_in_row.append(str(num))
            else:
                nums_in_row.append("X")
        print(", ".join(nums_in_row))
    print("=========================")

###############################################################################
# MAIN
###############################################################################


# ============================================================================
# CREATE INITIAL STRUCTURES
# ============================================================================

# 1) Number
# NB: there is no 0 in Sudoku! => each numbers value = idx+1 !
for i in range(0, SIZE):
    numbers.append(Number(i+1, SIZE))
# special number: None = no number
no_number = Number(None, SIZE)

# 2) Cell -> Number
for row in range(0, SIZE):
    cells_in_row = []
    for col in range(0, SIZE):
        # create cell initially with no number(None)
        cells_in_row.append(Cell(no_number))
    cells.append(cells_in_row)

# 3.1) Row -> Cell -> Number
for row_idx in range(0, SIZE):
    rows.append(Row(row_idx, cells[row_idx]))

# 3.2) Column -> Cell -> Number
temp_columns = []

for col_idx in range(0, SIZE):
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


# Connect Cell <-> Row / Column / Square
for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        cells[row_idx][col_idx].row(rows[row_idx])
        cells[row_idx][col_idx].column(columns[col_idx])
        cells[row_idx][col_idx].square(squares[row_idx//helpers.get_square_size()][col_idx//helpers.get_square_size()])


# ============================================================================
# FILL INITIAL NUMBERS
# ============================================================================

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        number = get_number(SUDOKU[row_idx][col_idx])
        cell = cells[row_idx][col_idx]
        update_cell(cell, number)
        if number.has_value():
            num_fixed_cells += 1


# ============================================================================
# CREATE CANDIDATES
# ============================================================================

print_sudoku()
print("initially", num_fixed_cells, "cells (", round((num_fixed_cells*100)/(SIZE*SIZE),2), "%) completed!")

for turn_it in range(0,5):

    for row_idx in range(0, SIZE):
        for col_idx in range(0, SIZE):
            cell = cells[row_idx][col_idx]
            cell.clear_candidates()
            if not cell.is_fix():
                # initially: 10 candidates (each possible number)
                candidates = []
                for number in numbers:
                    candidates.append(number)
                # each number only once per row
                for row_cell in cell.row().cells():
                    if row_cell.is_fix() and row_cell.number() in candidates:
                        candidates.remove(row_cell.number())
                # each number only once per column
                for column_cell in cell.column().cells():
                    if column_cell.is_fix() and column_cell.number() in candidates:
                        candidates.remove(column_cell.number())
                # each number only once per square
                for i in range(0, helpers.get_square_size()):
                    for j in range(0, helpers.get_square_size()):
                        square_cell = cell.square().cell(i,j)
                        if square_cell.is_fix() and square_cell.number() in candidates:
                            candidates.remove(square_cell.number())

                '''
                nc = []
                for c in candidates:
                    nc.append(str(c.value()))
                print(row_idx, col_idx, "|", ", ".join(nc), "|", len(nc))
                '''

                # solve cell or save candidates
                if len(candidates) == 1:
                    update_cell(cell, candidates[0])
                    num_fixed_cells += 1
                    # print("update", cell.row().idx(), cell.column().idx(), cell.number().value())
                if len(candidates) == 0:
                    sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")
                else:
                    for candidate in candidates:
                        cell.add_candidate(candidate)

    print("after", turn_it+1, "turns", num_fixed_cells, "cells (", round((num_fixed_cells*100)/(SIZE*SIZE),2), "%) completed!")

print_sudoku()

# test prints
# print(cells[3][4].number().value())
# print(cells[3][4].row().column(4).number().value())
# print(cells[3][4].column().row(3).number().value())
# print(rows[3].column(4).number().value())
# print(columns[4].row(3).number().value())
# print(squares[0][1].cell(1,2).number().value())
# print(numbers[2].counter())
# print(cells[1][7].number().value())
