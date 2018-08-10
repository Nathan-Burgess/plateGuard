# Buffer class, holds 2 seconds of video and processes to encrypt

from car import *
from coordRetrv import *
from pilEncrypt import *
import cv2
import sys
from statistics import mode
import time


class Buffer:
    def __init__(self):
        self.frame = []         # Holds each frame for the 2 second buffer
        self.final_plate = []   # Holds the final moded plate number from cars
        self.car = [Car() for i in range(10)]
        self.tracker = [cv2.TrackerKCF_create() for i in range(10)]
        self.counter = 0
        self.track_counter = 0
        self.bbox = (-1, -1, -1, -1) # TODO Fix this for multiplates

    # Assigns new results from openALPR to correct car object
    # by finding nearest neighbor withing delta_min/delta_max
    def calculate_knn(self, results):
        for plate in results:
            min = sys.maxsize
            num = 0
            coord = plate['coordinates']
            a = coord[0]
            b = coord[2]
            x = a['x']
            x2 = b['x']
            y = a['y']
            y2 = b['y']
            width = x2 - x
            height = y2 - y
            LP = plate['plate']
            # Loops through cars to find nearest neighbor
            for n, car in enumerate(self.car):
                if car.coords[self.counter-1][0] != -1:
                    d = abs(x - car.coords[self.counter-1][0])
                    d += abs(y - car.coords[self.counter-1][1])
                    d = d / 2

                    if d < min:
                        min = d
                        num = n

            print("Min: ", min)
            print("delta_min: ", self.car[num].delta_min)
            print("delta_max: ", self.car[num].delta_max)
            if min > self.car[num].delta_min and min < self.car[num].delta_max:
                self.bbox = (x, y, width, height)
                self.update_car(num, self.bbox, LP)
                return
            else:
                print("different car...")


    # Starts tracker/runs openalpr for the initial coordinate
    def start(self, conf, runtime):
        print("starting...")
        start = time.time()
        results = coordRetrv(conf, runtime, self.frame[-1])
        finish = time.time()
        print("Time taken: ", finish-start)
        self.tracker = [cv2.TrackerKCF_create() for i in range(10)]
        n = 0

        if self.counter-1 > 0:
            self.calculate_knn(results)
        else:
            for plate in results:
                coord = plate['coordinates']
                LP = plate['plate']
                a = coord[0]
                b = coord[2]
                x1 = a['x']
                x2 = b['x']
                y1 = a['y']
                y2 = b['y']

                # Define initial box with coords of plate
                self.bbox = (x1, y1, (x2 - x1), (y2 - y1))
                self.update_car(n, self.bbox, LP)
                break       # TODO remove when multi-plate



        # initialize tracker for each found plate
        for i in range(len(results)):
            print('results', len(results), 'i', i)
            self.tracker[i].init(self.frame[-1], self.bbox)
            print('tracker', self.tracker[i])

    # updates the trackers, goes to start if tracker dies
    def update(self, conf, runtime):
        print("updating...")
        # calls start every 6 frames # TODO update to dynamic counts
        print(self.counter)
        if (self.counter+1) % 6 == 0:
            print("Reached 6 Frames")
            self.start(conf, runtime)
        else:
            # Go through each tracker to update the coordinates
            for i in range(1):

                ok, self.bbox = self.tracker[i].update(self.frame[-1])
                print(ok)

                # Checks if tracker is still working
                # Updates the car object if it is
                if ok:
                    self.update_car(i, self.bbox)
                    print('Updated')
                # If it is not okay starts a new counter
                # Only runs openALPR every 6 frames if tracker drops
                # TODO: update to dynamic counts?
                else:
                    print("Error: Lost Tracker")
                    if self.track_counter == 0:
                        self.start(conf, runtime)

                    if self.track_counter < 6:
                        self.track_counter += 1
                    else:
                        self.track_counter = 0
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
        print("Calculating deltas")
        self.car[n].calculate_delta(self.counter-1)

    def processing(self, out):
        # for i in range(len(self.car)-1):
        #     self.final_plate[i] = mode(self.car[i].plate)
        data = ''
        try:
            print("PLATES: ", self.car[0].plate)
            data = mode(self.car[0].plate)
        except:
            print("mode function invalid")
            data = 'halo'

        print("data", data)
        # self.final_plate.append(mode(self.car[0].plate))
        self.final_plate.append(data)

        for i in range(self.counter-1):
            tempframe = pilEncrypt(self.final_plate[0], self.frame[i], self.car[0].coords[i])
            out.write(tempframe)