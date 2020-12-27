import math

class Helpers():

    def __init__ (self, size):
        self.size_ = size

    def get_sudoku_size(self):
        return self.size_

    def get_square_size(self):
        return int(math.sqrt(self.size_))
