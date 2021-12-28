#!/usr/bin/env python3

class Number():

    # CONSTRUCTORs
    def __init__ (self, value=0):
        # row, column and box will later be set by actual Row and Column
        self.value_ = value
        self.columns_ = None
        self.rows_ = None
        self.boxs_ = None

    def set_structures(self, row, column, box):
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

    # Number (fixed)
    # TODO: own structure Number cares about error handling
    def number(self, number=None):
        if type(number) == int:
            self.number_ = number
        else:
            return self.number_

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
