#!/usr/bin/env python3

###############################################################################
# IMPORTS
###############################################################################

# Classes
from Sudoku import *
from structure.Cell import Cell
from structure.Line import Line
from structure.Box import Box
# from structure.Number import Number

# Helpers
import sys
import math


###############################################################################
# GLOBAL VARIABLES
###############################################################################

SIZE = 9

SUDOKU = SUDOKU_MEDIUM_HARD

numbers = []
cells = []
rows = []
columns = []
boxes = []

num_fixed_cells = 0
num_turns = 0


###############################################################################
# FUNCTIONS
###############################################################################

# ============================================================================
# update cell number => update all dependencies
# ============================================================================
def update_cell(cell, number):
    # Cell <-> Number
    # => Row / Column / Box updates automatically ?
    cell.number(number)
    # remove all candidates



# ============================================================================
# print current status of sudoku
# ============================================================================
def print_sudoku(label=""):
    global num_fixed_cells
    global num_turns
    global SIZE

    print("=================")
    for row_idx in range(0, SIZE):
        nums_in_row = []
        for col_idx in range(0, SIZE):
            num = cells[row_idx][col_idx].number()
            if num:
                nums_in_row.append(str(num))
            else:
                nums_in_row.append("·")
        print(" ".join(nums_in_row))
    print("=================")
    print(label, "turn number", num_turns, "|", num_fixed_cells, "cells (", round((num_fixed_cells*100)/(SIZE*SIZE),2), "% ) completed!")
    print("\n")


###############################################################################
# MAIN
###############################################################################


# ============================================================================
# CREATE INITIAL STRUCTURES
# ============================================================================

# Cell -> Number
for row in range(0, SIZE):
    cells_in_row = []
    for col in range(0, SIZE):
        # Number
        # NB: there is no 0 in Sudoku! => each number's value = idx+1 !
        numbers = []
        for i in range(0, SIZE):
            numbers.append(i+1)
        # construct cell with potentially all numbers as candidates
        cells_in_row.append(Cell(numbers))
    cells.append(cells_in_row)

# Row -> Cell -> Number
for row_idx in range(0, SIZE):
    rows.append(Line(row_idx, cells[row_idx]))

# Column -> Cell -> Number
temp_columns = []

for col_idx in range(0, SIZE):
    temp_columns.append([])

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        temp_columns[col_idx].append(cells[row_idx][col_idx])

for col_idx in range(0, SIZE):
    columns.append(Line(col_idx, temp_columns[col_idx]))

del temp_columns

# Box -> Cell -> Number
box_size = int(math.sqrt(SIZE))

# prepare structure: box[x][y]
for box_row in range(0, box_size):
    boxes.append([])
    for box_col in range(0, box_size):
        boxes[box_row].append([])

# fill boxes with inner boxes
for outer_box_row_idx in range(0, box_size):
    for outer_box_col_idx in range(0, box_size):
        # for each outer box: prepare inner box (same size)
        inner_box = []
        for inner_box_row in range(0, box_size):
            inner_box.append([])
            for inner_box_col in range(0, box_size):
                inner_box[inner_box_row].append([])
        # for each inner box: obtain inner box containing n cells
        for inner_box_row_idx in range(0, box_size):
            for inner_box_col_idx in range(0, box_size):
                cell = cells[outer_box_row_idx*box_size + inner_box_row_idx][outer_box_col_idx*box_size + inner_box_col_idx]
                inner_box[inner_box_row_idx][inner_box_col_idx] = cell
        # create new Box
        new_box = Box(outer_box_row_idx, outer_box_col_idx, inner_box)
        boxes[outer_box_row_idx][outer_box_col_idx] = new_box


# Connect Cell <-> Row / Column / Box
for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        cells[row_idx][col_idx].set_structures(
            rows[row_idx],          # row
            columns[col_idx],       # column
            boxes[row_idx//box_size][col_idx//box_size]
        )


# ============================================================================
# FILL INITIAL NUMBERS
# ============================================================================

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        # TODO: own structure: Number that cares about error handling
        # get numbers from original Sudoku
        cell_value = SUDOKU[row_idx][col_idx]

        # set actual number
        try:
            number = int(cell_value)
            # error handling: number must be in range
            if number < 0 or number > SIZE:
                sys.exit("Error: number", number, "not in range of this Sudoku")

        # if no number is given => empty cell => 0
        except:
            number = 0

        # print(number)

        cell = cells[row_idx][col_idx]
        update_cell(cell, number)

        if number > 0:
            num_fixed_cells += 1

# ============================================================================
# CREATE CANDIDATES
# ============================================================================
print_sudoku("INIT ")

# --------------------------------------------------------------------------
# 1) CANDIDATE ELIMINATION
#    straightforward approach: create potential candidates for each cell
#    sucessively remove all impossible candidates
#    => if only one candidate remains: assign it!
# --------------------------------------------------------------------------

turn_has_improved = True
while turn_has_improved and num_fixed_cells < SIZE*SIZE:

    turn_has_improved = False
    for row_idx in range(0, SIZE):
        for col_idx in range(0, SIZE):
            cell = cells[row_idx][col_idx]
            if not cell.is_fix():
                # each number only once per row
                # => remove each number in row from list of candiates
                for idx in range(0, SIZE):
                    row_cell = cell.row().cell(idx)
                    if row_cell.is_fix():
                        cell.remove_candidate(row_cell.number())
                # each number only once per column
                # => remove each number in column from list of candiates
                for idx in range(0, SIZE):
                    column_cell = cell.column().cell(idx)
                    if column_cell.is_fix():
                        cell.remove_candidate(column_cell.number())
                # each number only once per box
                # => remove each number in box from list of candiates
                for i in range(0, box_size):
                    for j in range(0, box_size):
                        box_cell = cell.box().cell(i,j)
                        if box_cell.is_fix():
                            cell.remove_candidate(box_cell.number())

                # solve cell
                if cell.num_candidates() == 0:
                    sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")
                elif cell.num_candidates() == 1:
                    update_cell(cell, cell.candidates()[0])
                    num_fixed_cells += 1
                    turn_has_improved = True

    num_turns += 1
    print_sudoku("AFTER CELL CANDIDATE ELIMINATION")
'''
            print_str = ""
            if cell.is_fix():
                print_str = "FIX: " + str(cell.number())
            else:
                cs = cell.candidates()
                c_str = []
                for c in cs:
                    c_str.append(str(c.value()))
                print_str = ", ".join(c_str)
            print("Z", cell.row().idx()+1, "S", cell.column().idx()+1, ": ", print_str)

    print("after", num_turns, "turns (1.0)", num_fixed_cells, "cells (", round((num_fixed_cells*100)/(SIZE*SIZE),2), "%) completed!")
'''
# --------------------------------------------------------------------------
# 2) NUMBER ELIMINATION
#    check for each row/column/box:
#       each number must appear exactly once
#       -> determine how many candidates within the row/column/box there are
#       => if only one candidate remains: assign it!
# --------------------------------------------------------------------------

turn_has_improved = True
while turn_has_improved and num_fixed_cells < SIZE*SIZE:
    turn_has_improved = False

    # ----------------------------------------------------------------------
    # Number elimination: Column
    # ----------------------------------------------------------------------

    for column in columns:
        # check for each number if it is already present in the column
        numbers_left = []
        for number in numbers:
            if not column.has_number(number):
                numbers_left.append(number)
        # check for each left over number how many potential candidates
        # there are in the column
        for number in numbers_left:
            candidates = []
            # check for each cell if
            # 1. empty, 2. number not is in this row and 3. not in this box
            for cell_idx in range(0, SIZE):
                cell = column.cell(cell_idx)
                if not cell.is_fix() and not cell.row().has_number(number) and not cell.box().has_number(number):
                    candidates.append(cell)
            # if only one candidate => set it!
            if len(candidates) == 1:
                update_cell(candidates[0], number)
                num_fixed_cells += 1
                turn_has_improved = True
            if len(candidates) == 0:
                sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")
            # TODO: update candidates for cell? for numbers?

    num_turns += 1
    print_sudoku("AFTER NUMBER ELIMINATION (COLUMNS)")


    # ----------------------------------------------------------------------
    # Number elimination: Row
    # ----------------------------------------------------------------------

    for row in rows:
        # check for each number if it is already present in the row
        numbers_left = []
        for number in numbers:
            if not row.has_number(number):
                numbers_left.append(number)
        # check for each left over number how many potential candidates
        # there are in the row
        for number in numbers_left:
            candidates = []
            # check for each cell if
            # 1. empty, 2. number not is in this column and 3. not in this box
            for row_idx in range(0, SIZE):
                cell = row.cell(row_idx)
                if not cell.is_fix() and not cell.column().has_number(number) and not cell.box().has_number(number):
                    candidates.append(cell)
            # if only one candidate => set it!
            if len(candidates) == 1:
                update_cell(candidates[0], number)
                num_fixed_cells += 1
                turn_has_improved = True
            if len(candidates) == 0:
                sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")

    num_turns += 1
    print_sudoku("AFTER NUMBER ELIMINATION (ROWS)")

    # ----------------------------------------------------------------------
    # Number elimination: Box
    # ----------------------------------------------------------------------

    for box_row in boxes:
        for box in box_row:
            # check for each number if it is already present in the box
            numbers_left = []
            for number in numbers:
                if not box.has_number(number):
                    numbers_left.append(number)

            # check for each left over number how many potential candidates
            # there are in the row
            for number in numbers_left:
                candidates = []
                # check for each cell if
                # 1. empty, 2. number not is in this column and 3. not in this box
                for row_idx in range(0, box_size):
                    for col_idx in range(0, box_size):
                        cell = box.cell(row_idx, col_idx)
                        if not cell.is_fix() and not cell.column().has_number(number) and not cell.row().has_number(number):
                            candidates.append(cell)
                # if only one candidate => set it!
                if len(candidates) == 1:
                    update_cell(candidates[0], number)
                    num_fixed_cells += 1
                    turn_has_improved = True
                if len(candidates) == 0:
                    sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")

    num_turns += 1
    print_sudoku("AFTER NUMBER ELIMINATION (SQARES)")

# --------------------------------------------------------------------------
# 3) BACKTRACKING
#    for all remaning non-fixed cells:
#       pick one with a minumum number of candidates
#       randomly guess one number
#       save the state
#       check if sudoku can be solved
#           if error: trace back to state and guess other number
# --------------------------------------------------------------------------


'''
print_sudoku()

# test prints
# print(cells[3][4].number())
# print(cells[3][4].row().column(4).number())
# print(cells[3][4].column().row(3).number())
# print(rows[3].column(4).number())
# print(columns[4].row(3).number())
# print(boxes[0][1].cell(1,2).number())
# print(numbers[2].counter())
# print(cells[1][7].number())
'''
