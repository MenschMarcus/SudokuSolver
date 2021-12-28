#!/usr/bin/env python3
# duty: setup all structures properly and handle errors
import math

from structure.Cell import Cell
from structure.Line import Line
from structure.Box import Box

# ==============================================================================

class StructureManager():

    # ==========================================================================
    # CONSTRUCTOR
    # ==========================================================================
    def __init__(self, size=0):

        # error handling: sudoku size must be square number
        if int(math.sqrt(size)) - math.sqrt(size) != 0:
            sys.error("ERROR: sudoko size not a square number!")

        # setup size of sudoko and of each box within the sudoku
        self.size_ = size
        self.box_size_ = int(math.sqrt(size))


    # ==========================================================================
    # MAIN FUNCTION: setup all structures
    # ==========================================================================
    def setup(self, numbers):
        cells = []
        rows = []
        columns = []
        boxes = []

        # setup Cells with Numbers
        # ----------------------------------------------------------------------
        for row in range(0, self.size_):
            cells_in_row = []
            for col in range(0, self.size_):
                cells_in_row.append(Cell(numbers))
            cells.append(cells_in_row)

        # setup Rows with Cells
        # ----------------------------------------------------------------------
        for row_idx in range(0, self.size_):
            rows.append(Line(row_idx, cells[row_idx]))

        # setup Columns with Cells
        # ----------------------------------------------------------------------
        temp_columns = []

        # create column with empty cells
        for col_idx in range(0, self.size_):
            temp_columns.append([])

        # fill column with designated cell
        for row_idx in range(0, self.size_):
            for col_idx in range(0, self.size_):
                temp_columns[col_idx].append(cells[row_idx][col_idx])

        # finalize column
        for col_idx in range(0, self.size_):
            columns.append(Line(col_idx, temp_columns[col_idx]))

        # cleanup
        del temp_columns

        # setup Boxes with Cells
        # ----------------------------------------------------------------------

        # prepare structure: box[x][y]
        # create outer boxes
        for box_row in range(0, self.box_size_):
            boxes.append([])
            for box_col in range(0, self.box_size_):
                boxes[box_row].append([])

        # fill outer boxes with inner boxes
        for outer_box_row_idx in range(0, self.box_size_):
            for outer_box_col_idx in range(0, self.box_size_):
                # for each outer box: prepare inner box (same size)
                inner_box = []
                for inner_box_row in range(0, self.box_size_):
                    inner_box.append([])
                    for inner_box_col in range(0, self.box_size_):
                        inner_box[inner_box_row].append([])
                # for each inner box: obtain inner box containing n cells
                for inner_box_row_idx in range(0, self.box_size_):
                    for inner_box_col_idx in range(0, self.box_size_):
                        cell = cells[outer_box_row_idx*self.box_size_ + inner_box_row_idx][outer_box_col_idx*self.box_size_ + inner_box_col_idx]
                        inner_box[inner_box_row_idx][inner_box_col_idx] = cell
                # create new Box
                new_box = Box(outer_box_row_idx, outer_box_col_idx, inner_box)
                boxes[outer_box_row_idx][outer_box_col_idx] = new_box


        # connect Cell <-> Row / Column / Box
        # ----------------------------------------------------------------------
        for row_idx in range(0, self.size_):
            for col_idx in range(0, self.size_):
                cells[row_idx][col_idx].setup_structures(
                    rows[row_idx],          # row
                    columns[col_idx],       # column
                    boxes[row_idx//self.box_size_][col_idx//self.box_size_]
                )

        return [cells, rows, columns, boxes]
