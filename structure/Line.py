#!/usr/bin/env python3

class Line():

    def __init__ (self, idx, cells):
        self.idx_ = idx
        self.cells_ = cells

    # GETTER
    def idx(self):
        return self.idx_

    def cell(self, line_idx):
        return self.cells_[line_idx]

    def has_number(self, number):
        for cell in self.cells_:
            if cell.number() == number:
                return True
        return False
