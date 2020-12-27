#!/usr/bin/env python3

class Number():

    # CONSTRUCTOR
    def __init__ (self, value):
        if value:
            self.value_ = value
        else:
            self.value_ = None
        self.counter_ = 0

    # GETTER
    def value(self):
        return self.value_

    def counter(self):
        return self.counter_

    # SETTER
    def increase(self):
        self.counter_ += 1

    def decrease(self):
        self.counter_ -= 1
