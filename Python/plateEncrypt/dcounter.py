"""
Class that controls how often ALPR is run, excluding tracker failure
"""


class DCounter:
    def __init__(self):
        self.counter = 0
        self.max = 1
        self.alpr_minimum_run = 30

    def update_counter(self):
        if self.max < self.alpr_minimum_run:
            self.max *= 3
            if self.max > self.alpr_minimum_run:
                self.max = self.alpr_minimum_run
        # else:
        #     self.max = 1
