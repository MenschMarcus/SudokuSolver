#!/usr/bin/env python3

###############################################################################
# IMPORTS
###############################################################################

from number.Number import Number
from structure.Line import Line
from structure.Square import Square


###############################################################################

class Cell():

    # CONSTRUCTOR
    def __init__ (self, number):
        # row and column will later be set by actual Row and Column
        self.row_ = None
        self.column_ = None
        self.number_ = number
        self.candidates_ = []

    # GETTER
    def is_fix(self):
        return self.number_.value() != None

    # MAIN DEPENDENCIES: Cell n:1 Row, Column, Square, Number
    def number(self, number=None):
        if type(number) == Number:
            self.number_ = number
        else:
            return self.number_

    def row(self, row=None):
        if type(row) == Line:
            self.row_ = row
        else:
            return self.row_

    def column(self, column=None):
        if type(column) == Line:
            self.column_ = column
        else:
            return self.column_

    def square(self, square=None):
        if type(square) == Square:
            self.square_ = square
        else:
            return self.square_

    # Candidates
    def add_candidate(self, number):
        self.candidates_.append(number)

    def remove_candidate(self, number):
        self.candidates_.remove(number)

    def clear_candidates(self):
        self.candidates_ = []

    def num_candidates(self):
        return len(self.candidates_)

    def get_candidates(self):
        return self.candidates_
