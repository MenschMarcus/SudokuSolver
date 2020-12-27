#!/usr/bin/env python3

class Row():

    def __init__ (self, id, cells):
        self.id_ = id
        self.cells_ = cells

    # GETTER
    def id(self):
        return self.id_

    def column(self, column_id):
        return self.cells_[column_id]
