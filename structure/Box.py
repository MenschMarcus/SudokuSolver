#!/usr/bin/env python3

class Box():

    # CONSTRUCTOR
    def __init__ (self, row, column, cells):
        self.row_idx_ = row        # 1 … 3
        self.column_idx_ = column  # 1 … 3
        self.cells_ = cells        # 1 … 9

    # GETTER
    def cell(self, row, column):
        return self.cells_[row][column]

    def has_number(self, number):
        for cell_row in self.cells_:
            for cell_col in cell_row:
                if cell_col.number() == number:
                    return True
        return False
