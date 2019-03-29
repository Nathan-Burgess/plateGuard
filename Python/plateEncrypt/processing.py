"""
Manages processing of incoming frames, lp detection and encryption
"""

import unittest
import buffer
import cv2
import detect
import car as CAR
import random
import sys
import encrypt
from statistics import mode


# Calls openALPR and appends results to self.results
def call_detect(buff):
    # Gets results from openALPR
    for i in range(len(buff.frames)):
        result = detect.detect(buff.frames[i])
        if result:
            # Saves results to car per frame
            calculate_knn(buff, result, i)

      #  print(result)
       # for plate in result:
        #    buff.cars[0].coords[i] = plate['coordinates']
         #   buff.cars[0].final_plate = plate['plate']
            # buff.cars.append(CAR.Car(plate['plate'], plate['coordinates']))


# Blanks out license plate area after encrypting
def clear_plate_area(buff):
    for car in buff.cars:
        try:
            car.final_plate = mode(car.plate)
        except:
            car.final_plate = "halo"

    # Loop through all frames in buffer
    for i, frame in enumerate(buff.frames):
        # Loop through cars per frame
        for n, car in enumerate(buff.cars):
            strp = ""
            strc = ""
            # Get (x1,y1), (x2,y2) coordinates for each plate area
            if car.coords[i] is not -1:
                a, b, c, d = car.coords[i]
                x1 = int(a['x'])
                x2 = int(c['x'])
                y1 = int(a['y'])
                y2 = int(c['y'])
                strc = str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "*"

                # Blank each plate to static
                for x in range(x1, x2):
                    for y in range(y1, y2):
                        b, g, r = frame[y, x]
                        strp = strp + "(" + str(b) + "," + str(g) + "," + str(r) + "),"
                        frame.itemset((y, x, 0), random.randint(1, 255))
                        frame.itemset((y, x, 1), random.randint(1, 255))
                        frame.itemset((y, x, 2), random.randint(1, 255))

                # TODO - change to json dump in byte data
                strp = strp + "*"
                strf = car.final_plate + "*" + strc + strp
                # TODO, fix this garbage
                # TODO - just pass buff, n and json dump so we don't have to pass so many variables
                encrypt.encrypt(buff.frame_num + i, n, strf, car.final_plate, buff.encrypt_path)


# Assigns new results from openALPR to correct car object
# by finding nearest neighbor with delta_min/delta_max
def calculate_knn(buff, result, frame_count):
    if frame_count is 0:
        for i, plate in enumerate(result):
            buff.cars[i].coords[0] = plate['coordinates']
            buff.cars[i].plate.append(plate['plate'])
        return

    # Holds location of found plates to ensure not using same plate for multiple cars
    used_plates = [-1 for i in range(10)]
    for n, car in enumerate(buff.cars):
        coords = -1
        minimum = sys.maxsize
        lp = 'halo'
        # Check if coordinates are present for the plate
        if car.coords[frame_count-1] is not -1:
            # Loop through plates found
            for i, plate in enumerate(result):
                # See if the plate is already known
                if i not in used_plates:
                    a, b, c, d = plate['coordinates']
                    x = int(a['x'])
                    y = int(a['y'])

                    """
                    Calculates the delta from license plate coordinates
                    Average the two delta values
                    """
                    d = abs(x - car.coords[frame_count-1][0]['x'])
                    d += abs(y - car.coords[frame_count-1][0]['y'])
                    d = d/2

                    # Checks if the delta is less than the currently lowest delta
                    if d < minimum:
                        minimum = d
                        lp = plate['plate']
                        used_plates[n] = i
                        coords = plate['coordinates']
        else:
            break

        # Update car with license plate data
        car.coords[frame_count] = coords
        car.plate.append(lp)

    # Add new plates found
    for i in range(len(result)):
        if i not in used_plates:
            buff.cars[n].coords[frame_count] = result[i]['coordinates']
            buff.cars[n].plate.append(result[i]['plate'])
            n += 1


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
