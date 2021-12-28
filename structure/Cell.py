#!/usr/bin/env python3

class Cell():

    # CONSTRUCTORs
    def __init__ (self, numbers):
        # row, column and box will later be set by actual Row and Column
        self.row_ = None
        self.column_ = None
        self.box_ = None
        self.number_ = None
        self.candidates_ = numbers

    def setup_structures(self, row, column, box):
        self.row_ = row
        self.column_ = column
        self.box_ = box

    # GETTER
    def is_fix(self):
        return self.number_ != 0

    def row(self):
        return self.row_

    def column(self):
        return self.column_

    def box(self):
        return self.box_

    def candidates(self):
        return self.candidates_

    # Number
    def number(self, number):
        self.number_ = number

    # NumberCandidates
    def add_candidate(self, number):
        self.candidates_.append(number)

    def remove_candidate(self, number):
        if number in self.candidates_:
            self.candidates_.remove(number)

    def clear_candidates(self):
        self.candidates_ = []

    def num_candidates(self):
        return len(self.candidates_)
