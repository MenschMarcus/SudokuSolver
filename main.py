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

numbers = [None]    # number 0 not present in Sudoku! => first element "None"
cells = []
rows = []
columns = []
boxes = []


# =============================================================================
# SETUP STRUCTURES
# =============================================================================

# setup numbers
number_manager = NumberManager(SIZE)
numbers = number_manager.setup()

# setup structures: cells -> rows, columns, boxes
structure_manager = StructureManager(SIZE)
[cells, rows, columns, boxes] = structure_manager.setup()
box_size = structure_manager.get_box_size()

# initially setup candidates
for row_idx in range(0, SIZE):
    for col_idx in range(0, SIZE):
        for number in numbers:
            if number:
                cells[row_idx][col_idx].add_candidate(number)

# test printout
structure_manager.print_sudoku("INIT ", cells)

# =============================================================================
# FILL WITH CLUES FROM INITIAL SUDOKU
# =============================================================================

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

# test printout
structure_manager.print_sudoku("FILL ", cells)


# ============================================================================
# SOLUTION APPROACHES
# ============================================================================

# --------------------------------------------------------------------------
# 1) CANDIDATE ELIMINATION
#    straightforward approach: create potential candidates for each cell
#    sucessively remove all impossible candidates
#    => if only one candidate remains: assign it!
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# 2) REVERSE CANDIDATE ELIMINATION
#    check for each row/column/box:
#       each number must appear exactly once
#       -> determine how many candidates within the row/column/box there are
#       => if only one candidate remains: assign it!
# --------------------------------------------------------------------------

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
