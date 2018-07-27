# Buffer class, holds 2 seconds of video and processes to encrypt

from car import *
from coordRetrv import *
from pilEncrypt import *
import cv2
from statistics import mode

class Buffer:
    def __init__(self):
        self.frame = []         # Holds each frame for the 2 second buffer
        self.final_plate = []   # Holds the final moded plate number from cars
        self.car = [Car() for i in range(10)]
        self.tracker = [cv2.TrackerKCF_create() for i in range(10)]
        self.counter = 0
        self.bbox = (-1, -1, -1, -1) # TODO Fix this for multiplates

    # def test(self):
    #     for i in range(10):
    #         print(self.car[i].exists)

    # Starts tracker/runs openalpr for the initial coordinate
    def start(self, conf, runtime):
        print("starting...")
        results = coordRetrv(conf, runtime, self.frame[-1])

        n = 0

        for plate in results:
            coord = plate['coordinates']
            LP = plate['plate']
            self.update_car(n, coord, LP)
            a = coord[0]
            b = coord[2]
            x1 = a['x']
            x2 = b['x']
            y1 = a['y']
            y2 = b['y']
            break       # TODO remove when multiplate

        # Define initial box with coords of plate
        self.bbox = (x1, y1, (x2-x1), (y2-y1))

        # initialize tracker for each found plate
        for i in range(len(results)):
            self.tracker[i].init(self.frame[-1], self.bbox)

    # updates the trackers, goes to start if tracker dies
    def update(self, conf, runtime):
        print("updating...")
        # calls start every 6 frames # TODO update to dynamic counts
        if (self.counter+1) % 6 == 0:
            print("Fail 1")
            self.start(conf, runtime)
        else:
            # Go through each tracker to update the coordinates
            for i in range(0, len(self.tracker)):
                ok, self.bbox = self.tracker[i].update(self.frame[-1])

                if ok:
                    self.update_car(i, self.bbox)
                else:
                    print("Fail 2")
                    self.start(conf, runtime)
                    break


    # Inserts frame into the frame array
    def update_frame(self, frame):
        self.frame.append(frame)
        self.counter += 1

    # Updates car object with information for the car
    def update_car(self, n, coords, plate = None):
        self.car[n].coords[self.counter] = coords

        if plate != None:
            self.car[n].plate.append(plate)

    def processing(self, out):
        # for i in range(len(self.car)-1):
        #     self.final_plate[i] = mode(self.car[i].plate)
        self.final_plate.append(mode(self.car[0].plate))

        for i in range(self.counter+1):
            tempframe = pilEncrypt(self.final_plate[0], self.frame[i], self.car.coords[i])
            out.write(tempframe)