#!/usr/bin/env python3

class Cell():

    # CONSTRUCTOR
    def __init__ (self, row, column, number, is_fix=False):
        # initially only row and column id
        # -> will later be replaced by actual Row and Column
        self.row_id_ = row
        self.column_id_ = column
        self.row_ = None
        self.column_ = None
        self.number_ = number
        self.is_fix_ = is_fix

    # SETTER / GETTER
    def number(self, number=None):
        return self.number_

    def row(self):
        return self.row_

    def column(self):
        return self.column_

    # SETTER
