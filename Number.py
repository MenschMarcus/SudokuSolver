#!/usr/bin/env python3

import math

class Number():

    # CONSTRUCTOR
    def __init__ (self, value, max):

        if value >= 0 and value <= max:   # number from )0 to Sudoku SIZE)
            self.value_ = value
        else:       # None = no number
            self.value_ = None
        self.counter_ = 0

        # init structures
        self.cells_ = []
        self.rows_ = []
        self.columns_ = []
        for i in range(0, max):
            self.rows_.append(None)
            self.columns_.append(None)
            self.cells_.append([])
            for j in range(0, max):
                self.cells_[i].append(None)

        self.squares_ = []
        for i in range(0, int(math.sqrt(max))):
            self.squares_.append([])
            for j in range(0, int(math.sqrt(max))):
                self.squares_[i].append(None)

    # GETTER
    def value(self):
        return self.value_

    def counter(self):
        return self.counter_

    # SETTER
    def add_cell(self, cell):
        pass

    def increase(self):
        self.counter_ += 1

    def decrease(self):
        self.counter_ -= 1
