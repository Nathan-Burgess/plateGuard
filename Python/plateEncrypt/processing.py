"""
Manages processing of incoming frames, lp detection and encryption
"""

import unittest
import buffer
import cv2
import detect
import car
import random
import sys


# Calls openALPR and appends results to self.results
def call_detect(buff, frame_num):
    # Gets results from openALPR
    result = detect.detect(buff.frames[frame_num])
    # Saves results to car per frame
    # TODO Update to make sure it's working with actually multiple frames
    for plate in result:
        buff.cars.append(car.Car(plate['plate'], plate['coordinates']))


# Blanks out license plate area after encrypting
def clear_plate_area(buff):
    # TODO call encrypt for each plate

    # Loop through all frames in buffer
    for i, frame in enumerate(buff.frames):
        # Loop through cars per frame
        for n, car in enumerate(buff.cars):
            # Get (x1,y1), (x2,y2) coordinates for each plate area
            print(car.coords)
            a, b, c, d = car.coords
            x1 = int(a['x'])
            x2 = int(c['x'])
            y1 = int(a['y'])
            y2 = int(c['y'])

            # Blank each plate to black
            for x in range(x1, x2):
                for y in range(y1, y2):
                    b, g, r = frame[y, x]
                    frame.itemset((y, x, 0), random.randint(1, 255))
                    frame.itemset((y, x, 1), random.randint(1, 255))
                    frame.itemset((y, x, 2), random.randint(1, 255))

# Assigns new results from openALPR to correct car object
# by finding nearest neighbor with delta_min/delta_max
# def calculate_knn(self):
#     # Holds previously found license plates
#     used_plates = []
#     for car in self.car

"""
Unit tests for Processing class
"""


class TestProcessing(unittest.TestCase):

    def test_call_detect(self):
        # Read from video, just one frame to test
        cap = cv2.VideoCapture("../../test_plates/test_video_short.mp4")
        ret, frame = cap.read()
        self.assertTrue(ret)

        buff = buffer.Buffer()

        buff.frames.append(frame)

        call_detect(buff, 0)
        plate = buff.cars[0].plate

        self.assertEqual("JTX0178", plate)

    def test_clear_plate_area(self):
        # Read from video, just one frame to test
        cap = cv2.VideoCapture("../../test_plates/test_video_short.mp4")
        ret, frame = cap.read()
        self.assertTrue(ret)

        buff = buffer.Buffer()

        buff.frames.append(frame)

        call_detect(buff, 0)

        clear_plate_area(buff)
        cv2.imwrite("test_picture.jpg", buff.frames[0])


if __name__ == "__main__":
    unittest.main()
