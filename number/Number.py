#!/usr/bin/env python3

import math

class Number():

    # CONSTRUCTOR
    def __init__ (self, value, max):

        if value in range(1, max+1):   # number from 0 to (Sudoku SIZE)
            self.value_ = value
        else:       # None = no number
            self.value_ = None
        self.counter_ = 0

        # init cells[row][col] structure
        self.cells_ = []
        for i in range(0, max):
            self.cells_.append([])
            for j in range(0, max):
                self.cells_[i].append(None)

    # GETTER
    def value(self):
        return self.value_

    def has_value(self):
        return type(self.value_) == int

    def counter(self):
        return self.counter_

    # SET CELLS
    def add_cell(self, row_idx, col_idx, cell):
        self.cells_[row_idx][col_idx] = cell
        self.counter_ += 1

    def remove_cell(self, row_idx, col_idx):
        self.cells_[row_idx][col_idx] = None
        self.counter_ -= 1




'''
        self.rows_ = []
        self.columns_ = []
        self.squares_ = []
        for i in range(0, max):
            self.rows_.append(None)
            self.columns_.append(None)
            self.cells_.append([])
            for j in range(0, max):
                self.cells_[i].append(None)

        for i in range(0, int(math.sqrt(max))):
            self.squares_.append([])
            for j in range(0, int(math.sqrt(max))):
                self.squares_[i].append(None)
'''
