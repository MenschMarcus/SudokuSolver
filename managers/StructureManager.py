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

        # number of fixed cells
        self.num_fixed_cells_ = 0


    # ==========================================================================
    # MAIN FUNCTION: setup all structures
    # ==========================================================================

    def setup(self):

        cells = []
        rows = []
        columns = []
        boxes = []

        # ----------------------------------------------------------------------
        # setup Cells with Numbers
        # ----------------------------------------------------------------------
        for row in range(0, self.size_):
            cells_in_row = []
            for col in range(0, self.size_):
                cells_in_row.append(Cell())
            cells.append(cells_in_row)

        # ----------------------------------------------------------------------
        # setup Rows with Cells
        # ----------------------------------------------------------------------
        for row_idx in range(0, self.size_):
            rows.append(Line(row_idx, cells[row_idx]))

        # ----------------------------------------------------------------------
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

        # ----------------------------------------------------------------------
        # setup Boxes with Cells
        # ----------------------------------------------------------------------

        # prepare structure: box[x][y]
        # create outer boxes
        for box_row in range(0, self.box_size_):
            box = []
            for box_col in range(0, self.box_size_):
                box.append([])
            boxes.append(box)

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


        # ----------------------------------------------------------------------
        # connect Cell <-> Row / Column / Box
        # ----------------------------------------------------------------------
        for row_idx in range(0, self.size_):
            for col_idx in range(0, self.size_):
                cells[row_idx][col_idx].setup_structures(
                    rows[row_idx],
                    columns[col_idx],
                    boxes[row_idx//self.box_size_][col_idx//self.box_size_]
                )

        return [cells, rows, columns, boxes]


    # ==========================================================================
    # MAIN FUNCTION: update Cell <-> Number
    # ==========================================================================

    def update(self, cell, number, check_row=None, check_num=None):

        # case 1) empty -> empty    -> nothing to do
        # case 2) empty -> fix      -> update cell + add structures to row
        # case 3) fix -> empty      -> impossible!
        # case 4) fix -> fix        -> almost impossible!

        # case 2
        if number is not None:
            self.num_fixed_cells_ += 1

            # update number in cell
            cell.fix(number)
            cell.clear_candidates()

            # add structures to number
            number.add_row(cell.row().idx())
            number.add_column(cell.column().idx())
            number.add_box(cell.box().idx())


    # ==========================================================================
    # HELPER FUNCTION
    # ==========================================================================

    def print_sudoku(self, label="", cells=None):

        print("=================")
        for row_idx in range(0, self.size_):
            nums_in_row = []
            for col_idx in range(0, self.size_):
                cell = cells[row_idx][col_idx]
                if cell.is_fix():
                    nums_in_row.append(str(cell.number().value()))
                else:
                    nums_in_row.append("·")
            print(" ".join(nums_in_row))
        print("=================")
        print(label, "|", self.num_fixed_cells_, "cells (", round((self.num_fixed_cells_*100)/(self.size_*self.size_),1), "% ) completed!")
        print("\n")


    # ==========================================================================
    # GETTER
    # ==========================================================================

    def get_num_fixed_cells(self):
        return self.num_fixed_cells_

    def get_box_size(self):
        return self.box_size_
