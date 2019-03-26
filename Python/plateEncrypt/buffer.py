'''
Holds car and frame objects
'''

import car
import unittest


class Buffer:

    def __init__(self):
        self.cars = [car.Car() for i in range(10)]
        self.frames = []
        self.frame_num = 0


class TestBuffer(unittest.TestCase):
    def test_init(self):
        buff = Buffer()
        buff.car = "car"
        buff.frames = "frame"
        self.assertEqual("car", buff.car)
        self.assertEqual("frame", buff.frames)


if __name__ == "__main__":
    unittest.main()