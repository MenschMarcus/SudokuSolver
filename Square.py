#!/usr/bin/env python3

class Square():

    # CONSTRUCTOR
    def __init__ (self, row, column, cells):
        self.row_idx_ = row
        self.column_idx_ = column
        self.cells_ = cells

    # GETTER
    def cell(self, row, column):
        return self.cells_[row][column]
