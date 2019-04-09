"""
Class that controls how often ALPR is run, excluding tracker failure
"""


class DCounter:
    def __init__(self):
        self.counter = 0
        self.max = 1

    def update_counter(self):
        if self.max <= 30:
            self.max *= 3
        else:
            self.max = 1