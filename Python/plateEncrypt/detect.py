"""
Runs openalpr to detect license plate number for cars
"""

import unittest
import sys
import cv2
from openalpr import Alpr
import json


def detect(frame, runtime):
    # Configure ALPR setting according to config file
    alpr = Alpr("us", "/usr/share/openalpr/config/openalpr.defaults.conf", runtime)

    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    # Get the top result from ALPR for each plate
    alpr.set_top_n(1)
    alpr.set_default_region("tx")

    # Loads results from the openALPR library
    success, img_numpy = cv2.imencode('.jpg',frame)
    img_binary = img_numpy.tostring()
    results = alpr.recognize_array(img_binary)

    results = results['results']

    return results


"""
Testing Functions
"""


class TestDetect(unittest.TestCase):

    def test_detect_license_plate(self):
        image_location = "/home/michael/Projects/plateGuard/test_plates/backup/ea7the.jpg"

        # Read from config file
        with open("config.json", "r") as read_file:
            config = json.load(read_file)

        frame = cv2.imread(image_location)

        if frame is None:
            print("Error loading image")
            sys.exit(1)

        results = detect(frame, config['runtime'])

        for plate in results:
            results = plate['plate']

        self.assertEqual("EA7THE", results)


if __name__ == '__main__':
    unittest.main()
