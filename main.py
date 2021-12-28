#!/usr/bin/env python3

###############################################################################
# IMPORTS
###############################################################################

# Classes
from Sudoku import *

from structure.Number import Number
from structure.Cell import Cell
from structure.Line import Line
from structure.Box import Box

from managers.NumberManager import NumberManager
from managers.StructureManager import StructureManager

# Helpers
import sys
import math


###############################################################################
# GLOBAL VARIABLES
###############################################################################

SUDOKU_ID = 3

SIZE = 9

numbers = [None]    # number 0 not present in Sudoku!
cells = []
rows = []
columns = []
boxes = []

num_turns = 0


# =============================================================================
# SETUP STRUCTURES
# =============================================================================

# setup numbers
number_manager = NumberManager(SIZE)
numbers = number_manager.setup()

# setup structures: cells -> rows, columns, boxes
structure_manager = StructureManager(SIZE)
[cells, rows, columns, boxes] = structure_manager.setup()

# initially setup candidates
for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        for number in numbers:
            if number:
                cells[row_idx][col_idx].add_candidate(number)

# fill with clues from initial sudoku ("clues")
sudoku = SUDOKUS[SUDOKU_ID]

for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        # get clue from original Sudoku -> Number
        clue = number_manager.check_number(sudoku[row_idx][col_idx])
        if clue is None:
            number = None
        else:
            number = numbers[clue]
        # get Cell
        cell = cells[row_idx][col_idx]
        # update Cell <-> Number
        structure_manager.update(cell, number)

box_size = structure_manager.get_box_size()

# test printout
structure_manager.print_sudoku("INIT ", cells)


# ============================================================================
# SOLUTION APPROACHES
# ============================================================================

# --------------------------------------------------------------------------
# 1) CANDIDATE ELIMINATION
#    straightforward approach: create potential candidates for each cell
#    sucessively remove all impossible candidates
#    => if only one candidate remains: assign it!
# --------------------------------------------------------------------------
turn_has_improved = True
while turn_has_improved:

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
                    structure_manager.update(cell, cell.candidate())
                    turn_has_improved = True

    num_turns += 1

structure_manager.print_sudoku("AFTER CELL CANDIDATE ELIMINATION", cells)

#             print_str = ""
#             if cell.is_fix():
#                 print_str = "FIX: " + str(cell.number())
#             else:
#                 cs = cell.candidates()
#                 c_str = []
#                 for c in cs:
#                     c_str.append(str(c.value()))
#                 print_str = ", ".join(c_str)
#             print("Z", cell.row().idx()+1, "S", cell.column().idx()+1, ": ", print_str)
#
#     print("after", num_turns, "turns (1.0)", num_fixed_cells, "cells (", round((num_fixed_cells*100)/(SIZE*SIZE),2), "%) completed!")
# '''
# # --------------------------------------------------------------------------
# # 2) NUMBER ELIMINATION
# #    check for each row/column/box:
# #       each number must appear exactly once
# #       -> determine how many candidates within the row/column/box there are
# #       => if only one candidate remains: assign it!
# # --------------------------------------------------------------------------
#
# turn_has_improved = True
# while turn_has_improved and num_fixed_cells < SIZE*SIZE:
#     turn_has_improved = False
#
#     # ----------------------------------------------------------------------
#     # Number elimination: Column
#     # ----------------------------------------------------------------------
#
#     for column in columns:
#         # check for each number if it is already present in the column
#         numbers_left = []
#         for number in numbers:
#             if not column.has_number(number):
#                 numbers_left.append(number)
#         # check for each left over number how many potential candidates
#         # there are in the column
#         for number in numbers_left:
#             candidates = []
#             # check for each cell if
#             # 1. empty, 2. number not is in this row and 3. not in this box
#             for cell_idx in range(0, SIZE):
#                 cell = column.cell(cell_idx)
#                 if not cell.is_fix() and not cell.row().has_number(number) and not cell.box().has_number(number):
#                     candidates.append(cell)
#             # if only one candidate => set it!
#             if len(candidates) == 1:
#                 update_cell(candidates[0], number)
#                 num_fixed_cells += 1
#                 turn_has_improved = True
#             if len(candidates) == 0:
#                 sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")
#             # TODO: update candidates for cell? for numbers?
#
#     num_turns += 1
#     print_sudoku("AFTER NUMBER ELIMINATION (COLUMNS)")
#
#
#     # ----------------------------------------------------------------------
#     # Number elimination: Row
#     # ----------------------------------------------------------------------
#
#     for row in rows:
#         # check for each number if it is already present in the row
#         numbers_left = []
#         for number in numbers:
#             if not row.has_number(number):
#                 numbers_left.append(number)
#         # check for each left over number how many potential candidates
#         # there are in the row
#         for number in numbers_left:
#             candidates = []
#             # check for each cell if
#             # 1. empty, 2. number not is in this column and 3. not in this box
#             for row_idx in range(0, SIZE):
#                 cell = row.cell(row_idx)
#                 if not cell.is_fix() and not cell.column().has_number(number) and not cell.box().has_number(number):
#                     candidates.append(cell)
#             # if only one candidate => set it!
#             if len(candidates) == 1:
#                 update_cell(candidates[0], number)
#                 num_fixed_cells += 1
#                 turn_has_improved = True
#             if len(candidates) == 0:
#                 sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")
#
#     num_turns += 1
#     print_sudoku("AFTER NUMBER ELIMINATION (ROWS)")
#
#     # ----------------------------------------------------------------------
#     # Number elimination: Box
#     # ----------------------------------------------------------------------
#
#     for box_row in boxes:
#         for box in box_row:
#             # check for each number if it is already present in the box
#             numbers_left = []
#             for number in numbers:
#                 if not box.has_number(number):
#                     numbers_left.append(number)
#
#             # check for each left over number how many potential candidates
#             # there are in the row
#             for number in numbers_left:
#                 candidates = []
#                 # check for each cell if
#                 # 1. empty, 2. number not is in this column and 3. not in this box
#                 for row_idx in range(0, box_size):
#                     for col_idx in range(0, box_size):
#                         cell = box.cell(row_idx, col_idx)
#                         if not cell.is_fix() and not cell.column().has_number(number) and not cell.row().has_number(number):
#                             candidates.append(cell)
#                 # if only one candidate => set it!
#                 if len(candidates) == 1:
#                     update_cell(candidates[0], number)
#                     num_fixed_cells += 1
#                     turn_has_improved = True
#                 if len(candidates) == 0:
#                     sys.exit("ERROR: no candidate for this cell left => probaly a typo in the initial Sudoku?")
#
#     num_turns += 1
#     print_sudoku("AFTER NUMBER ELIMINATION (SQARES)")
#
# # --------------------------------------------------------------------------
# # 3) BACKTRACKING
# #    for all remaning non-fixed cells:
# #       pick one with a minumum number of candidates
# #       randomly guess one number
# #       save the state
# #       check if sudoku can be solved
# #           if error: trace back to state and guess other number
# # --------------------------------------------------------------------------
#
# print_sudoku()
#
# # test prints
# # print(cells[3][4].number())
# # print(cells[3][4].row().column(4).number())
# # print(cells[3][4].column().row(3).number())
# # print(rows[3].column(4).number())
# # print(columns[4].row(3).number())
# # print(boxes[0][1].cell(1,2).number())
# # print(numbers[2].counter())
# # print(cells[1][7].number())
