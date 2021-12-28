#!/usr/bin/env python3
# NB: there is no 0 in Sudoku! => value range from 1-9

import math

class Number():

    # CONSTRUCTORs
    def __init__ (self, value, max):
        self.value_ = value     # actual value of the number (0 or 1 .. 9)

        # maximum number
        self.max_ = max

        # number already present in this column / row?
        self.in_column_ = []
        self.in_row_ = []
        for i in range(0, max-1):
            self.in_column_.append(False)
            self.in_row_.append(False)

        # number already present in this box?
        self.in_box_ = []
        for i in range(0, int(math.sqrt(max-1))):
            inner_box = []
            for j in range(0, int(math.sqrt(max-1))):
                inner_box.append(False)
            self.in_box_.append(inner_box)

    # GETTER
    def value(self):
        return self.value_

    def is_in_column(self, column_idx):
        if column_idx in range(0, self.max_):
            return self.in_column_[column_idx]
        else:
            sys.error("class Number: column index out of bounds")

    def is_in_row(self, row_idx):
        if row_idx in range(0, self.max_):
            return self.in_row_[row_idx]
        else:
            sys.error("class Number: row index out of bounds")

    def is_in_box(self, box_idx_out, box_idx_in):
        if box_idx_out in range (0, math.sqrt(self.max_)) and box_idx_in in range (0, math.sqrt(self.max_)):
            return self.in_box_[box_idx_out][box_idx_in]
        else:
            sys.error("class Number: box index out of bounds")
