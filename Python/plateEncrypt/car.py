"""
Holds car information found in buffer
"""

import sys
import unittest


class Car:

    def __init__(self):
        self.exists = [0 for i in range(60)]                # Which frames the car shows up in
        self.plate = []                                     # Plate numbers for each frame found in
        self.final_plate = ""
        self.coords = [(-1) for i in range(60)]    # Coordinates of plate area in each frame
        self.delta_min = sys.maxsize
        self.delta_max = 0


class TestCar(unittest.TestCase):

    def test_init(self):
        car = Car()
        self.assertTrue(True not in car.exists)
        self.assertTrue(len(car.plate) is 0)
        self.assertTrue(car.final_plate is "")

    def test_exists(self):
        car = Car()
        car.exists[15] = True
        self.assertTrue(car.exists[15])

    def test_add_plate(self):
        car = Car()
        car.plate.append("EA7THE")
        self.assertTrue("EA7THE" in car.plate)

    def test_coords(self):
        car = Car()
        car.coords[15] = (1, 5, 3, 2)
        self.assertTrue(car.coords[15] == (1, 5, 3, 2))


if __name__ == '__main__':
    unittest.main()
