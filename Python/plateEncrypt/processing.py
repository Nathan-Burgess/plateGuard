"""
Manages processing of incoming frames, lp detection and encryption
"""

import unittest
import buffer
import cv2

class Processing:
    def __init__(self):
        self.tracker