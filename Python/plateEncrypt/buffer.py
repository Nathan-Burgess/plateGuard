'''
Holds car and frame objects
'''

import car
import unittest

class Buffer:

    def __init__(self):
        self.cars = []
        self.frames = []


class TestBuffer(unittest.TestCase):
    def test_init(self):
        buff = Buffer()
        buff.car = "car"
        buff.frames = "frame"
        self.assertEquals("car", buff.car)
        self.assertEquals("frame", buff.frames)


if __name__ == "__main__":
    unittest.main()