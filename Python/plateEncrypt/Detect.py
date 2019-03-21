"""
Runs openalpr to detect license plate number for cars
"""

import unittest
import sys
import cv2
from openalpr import Alpr


def Detect(image_location = "/home/michael/Projects/plateGuard/test_plates/backup"):
    # Configure ALPR setting according to config file
    print("Test2")
    alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "~/openalpr/runtime_data/")

    print("Test")
    if alpr.is_loaded():
        print("Done loading")

    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    # Get the top result from ALPR for each plate
    alpr.set_top_n(1)
    alpr.set_default_region("tx")

    # Loads results from the openALPR library
    success, img_numpy = cv2.imencode('.jpg', image_location)
    img_binary = img_numpy.tostring()
    results = alpr.recognize_array(img_binary)

    results = results['results']

    print(results)
    print("Done")


if __name__ == '__main__':
    Detect()

"""
Testing Functions
"""

# class TestDetect(unittest.TestCase):
#
#     def test_detect_license_plate(self):
#
#         self.assertTrue()
