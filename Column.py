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
