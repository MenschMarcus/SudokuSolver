import math

class Helpers():

    def __init__ (self, size):
        self.size_ = size

    # ========================================================================
    # return dimensions of Sudoku
    # ========================================================================
    def get_sudoku_size(self):
        return self.size_

    def get_square_size(self):
        return int(math.sqrt(self.size_))

    # ========================================================================
    # check if number is correct correct Number object
    # ========================================================================
    def check_number(self, num):
        # error handling: ensure that Number is either
        # int between 0 and SIZE of Sudoko
        try:
            num = int(num)
            if num >= 0 and num <= self.size_:
                return num
            else:
                sys.exit("Error: number in Sudoku not in range")

        # OR: None
        except:
            return None
