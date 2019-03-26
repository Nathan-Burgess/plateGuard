"""
Manages processing of incoming frames, lp detection and encryption
"""

import unittest
import buffer
import cv2
import detect
import json
import car
import random


class Processing:
    def __init__(self, buff, out, config):
        self.buff = buff
        self.out = out
        self.config = config
        self.results = []

    # Calls openALPR and appends results to self.results
    def call_detect(self, frame_num):
        # Gets results from openALPR
        result = detect.detect(self.buff.frames[frame_num], self.config['runtime'])
        # Saves results to car per frame
        # TODO Update to make sure it's working with actually multiple frames
        for plate in result:
            self.buff.cars.append(car.Car(plate['plate'], plate['coordinates']))

    # Blanks out license plate area after encrypting
    def clear_plate_area(self):
        # TODO call encrypt for each plate

        # Loop through all frames in buffer
        for i, frame in enumerate(self.buff.frames):
            # Loop through cars per frame
            for n, car in enumerate(self.buff.cars):
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


"""
Unit tests for Processing class
"""


class TestProcessing(unittest.TestCase):
    def set_up(self):
        # Read from config file
        with open("config.json", "r") as read_file:
            config = json.load(read_file)

        # Set up buffer
        buff = buffer.Buffer()
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 29.8, (1920, 1080))

        self.proc = Processing(buff, out, config)

    def test_call_detect(self):
        # Read from video, just one frame to test
        cap = cv2.VideoCapture("../../test_plates/test_video_short.mp4")
        ret, frame = cap.read()
        self.assertTrue(ret)

        self.proc.buff.frames.append(frame)

        self.proc.call_detect(0)
        plate = self.proc.buff.cars[0].plate

        self.assertEqual("JTX017", plate)

    def test_clear_plate_area(self):
        # Read from video, just one frame to test
        cap = cv2.VideoCapture("../../test_plates/test_video_short.mp4")
        ret, frame = cap.read()
        self.assertTrue(ret)

        self.proc.buff.frames.append(frame)

        self.proc.call_detect(0)

        self.proc.clear_plate_area()
        cv2.imwrite("test_picture.jpg", self.proc.buff.frames[0])


if __name__ == "__main__":
    unittest.main()
