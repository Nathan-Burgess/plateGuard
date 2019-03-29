"""
Holds car information found in buffer
"""

import sys


class Car:

    def __init__(self):
        self.exists = [0 for i in range(60)]                # Which frames the car shows up in
        self.plate = []                                     # Plate numbers for each frame found in
        self.final_plate = ""
        self.coords = [(-1) for i in range(60)]    # Coordinates of plate area in each frame
        self.delta_min = sys.maxsize
        self.delta_max = 0

