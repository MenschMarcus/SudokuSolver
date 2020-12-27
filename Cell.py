#!/usr/bin/env python3

###############################################################################
# IMPORTS
###############################################################################

from Number import Number
from Row import Row
from Column import Column
from Square import Square


###############################################################################

class Cell():

    # CONSTRUCTOR
    def __init__ (self, number):
        # row and column will later be set by actual Row and Column
        self.row_ = None
        self.column_ = None
        self.number_ = number
        self.is_fix_ = False

    # MAIN DEPENDENCIES: Cell n:1 Row, Column, Square, Number
    def number(self, number=None, is_fix=False):
        if type(number) == Number:
            self.number_ = number
            self.is_fix_ = is_fix
        else:
            return self.number_

    def row(self, row=None):
        if type(row) == Row:
            self.row_ = row
        else:
            return self.row_

    def column(self, column=None):
        if type(column) == Column:
            self.column_ = column
        else:
            return self.column_

    def square(self, square=None):
        if type(square) == Square:
            self.square_ = square
        else:
            return self.square_
