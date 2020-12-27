#!/usr/bin/env python3

class Column():

    def __init__ (self, id, cells):
        self.id_ = id
        self.cells_ = cells

    # GETTER
    def id(self):
        return self.id_

    def row(self, row_id):
        return self.cells_[row_id]
