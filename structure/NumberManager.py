#!/usr/bin/env python3
# duty: setup numbers properly and handle errors

import math

from structure.Number import Number

# ==============================================================================

class NumberManager():

    # ==========================================================================
    # CONSTRUCTOR
    # ==========================================================================
    def __init__(self, size=0):

        # error handling: sudoku size must be square number
        if int(math.sqrt(size)) - math.sqrt(size) != 0:
            sys.error("ERROR: sudoko size not a square number!")

        self.max_ = size + 1


    # ==========================================================================
    # MAIN FUNCTION: setup numbers
    # ==========================================================================

    def setup(self):
        numbers = []

        # NB: numbers range from 1 to 9
        for num_idx in range(1, self.max_):
            numbers.append(Number(num_idx, self.max_))

        return numbers


    # ==========================================================================
    # HELPER FUNCTION: check if number is in range
    # ==========================================================================

    def check_number(self, number):
        # ensure data type int
        number = int(number)
        if number < 1 or number > self.size_:
            sys.exit("Error: number out of range of this Sudoku")
        else:
            return(number)
