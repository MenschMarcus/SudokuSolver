#!/usr/bin/env python3

class Cell():

    # ==========================================================================
    # CONSTRUCTORs
    # ==========================================================================
    def __init__ (self):
        # row, column and box will later be set by actual Row and Column
        self.row_ = None
        self.column_ = None
        self.box_ = None
        self.number_ = None
        self.candidates_ = []

    def setup_structures(self, row, column, box):
        self.row_ = row
        self.column_ = column
        self.box_ = box


    # ==========================================================================
    # FIX CELL
    # ==========================================================================

    # set number
    def fix(self, number):
        self.number_ = number

    # get number
    def number(self):
        return self.number_

    # check if number
    def is_fix(self):
        return self.number_ != None


    # ==========================================================================
    # STRUCTURES
    # ==========================================================================

    def row(self):
        return self.row_

    def column(self):
        return self.column_

    def box(self):
        return self.box_


    # ==========================================================================
    # CANDIDATES
    # ==========================================================================

    def add_candidate(self, number):
        self.candidates_.append(number)

    def remove_candidate(self, number):
        if number in self.candidates_:
            self.candidates_.remove(number)

    def clear_candidates(self):
        self.candidates_ = []

    # return one and only candidate
    def candidate(self):
        return self.candidates_[0]

    # return all candidates
    def candidates(self):
        return self.candidates_

    def num_candidates(self):
        return len(self.candidates_)
