#!/usr/bin/env python3

class Column():

    def __init__ (self, idx, cells):
        self.idx_ = idx
        self.cells_ = cells

    # GETTER
    def idx(self):
        return self.idx_

    def row(self, row_idx):
        return self.cells_[row_idx]

    def cells(self):
        return self.cells_

    def has_number(self, number):
        for cell in self.cells_:
            if cell.number() == number:
                return True
        return False
