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

    # SETTER / GETTER
    def number(self, number=None, is_fix=False):
        if type(number) == Number:
            self.number_ = number
            self.is_fix_ = is_fix
        else:
            return self.number_

    def row(self):
        return self.row_

    def column(self):
        return self.column_

    # SETTER
