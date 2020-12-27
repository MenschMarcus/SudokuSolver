#!/usr/bin/env python3

class Row():

    def __init__ (self, idx, cells):
        self.idx_ = idx
        self.cells_ = cells

    # GETTER
    def idx(self):
        return self.idx_

    def column(self, column_idx):
        return self.cells_[column_idx]

    def cells(self):
        return self.cells_

    def has_number(self, number):
        for cell in self.cells_:
            if cell.number() == number:
                return True
        return False
