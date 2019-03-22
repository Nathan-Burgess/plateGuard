"""
Manages processing of incoming frames, lp detection and encryption
"""

import unittest
import buffer
import cv2


class Processing:
    def __init__(self, buff, out):
        self.buff = buff
        self.out = out


class TestProcessing(unittest.TestCase):
    def test_init(self):
        buff = "test1"
        out = "test2"
        proc = Processing(buff, out)
        self.assertEqual(("test1","test2"), (proc.buff, proc.out))


if __name__ == "__main__":
    unittest.main()
