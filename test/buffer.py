# Buffer class, holds 2 seconds of video and processes to encrypt

from car import *
from coordRetrv import *
from pilEncrypt import *
import cv2
import sys
from statistics import mode
import time
import track_test



class Buffer:
    def __init__(self,count):
        self.frame = []         # Holds each frame for the 2 second buffer
        self.car = [Car() for i in range(10)]
        self.tracker = [cv2.TrackerKCF_create() for i in range(10)]
        self.frame_counter = 0
        self.track_counter = 0
        self.bbox = (-1, -1, -1, -1)  # TODO Fix this for multiplates
        self.run_count = count

    # Assigns new results from openALPR to correct car object
    # by finding nearest neighbor withing delta_min/delta_max
    def calculate_knn(self, results):
        used_plates = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        for n, car in enumerate(self.car):
            minimum = sys.maxsize
            lp = 'halo'
            if car.coords[self.frame_counter - 1][0] is not -1:
                for i, plate in enumerate(results):
                    if i not in used_plates:
                        x, y, width, height = self.convert_coords(plate['coordinates'])

                        d = abs(x - car.coords[self.frame_counter - 1][0])
                        d += abs(y - car.coords[self.frame_counter - 1][1])
                        d = d / 2

                        if d < minimum:
                            minimum = d
                            self.bbox = (x, y, width, height)
                            lp = plate['plate']
                            used_plates[n] = i
            else:
                break
            self.update_car(n, self.bbox, lp)

        for i in range(len(results)):
            if i not in used_plates:
                self.update_car(n, self.convert_coords(results[i]['coordinates']), results[i]['plate'])
                n += 1

    # Starts tracker/runs openalpr for the initial coordinate
    def start(self, conf, runtime):
        print("starting...")
        start = time.time()
        results = coordRetrv(conf, runtime, self.frame[-1])
        finish = time.time()
        track_test.log.alpr_print(self.frame_counter, self.run_count, results, finish-start)
        print("Time taken: ", finish-start)
        self.tracker = [cv2.TrackerKCF_create() for i in range(10)]
        n = 0

        if self.frame_counter-1 > 0:
            self.calculate_knn(results)
        else:
            for plate in results:
                lp = plate['plate']

                # Define initial box with coords of plate
                self.bbox = self.convert_coords(plate['coordinates'])
                self.update_car(n, self.bbox, lp)
                # break       # TODO remove when multi-plate

        # initialize tracker for each found plate

        for i in range(len(results)):
            self.tracker[i].init(self.frame[-1], self.bbox)
            if i is 10:
                break

    # updates the trackers, goes to start if tracker dies
    def update(self, conf, runtime):
        print("updating...")
        # calls start every 6 frames # TODO update to dynamic counts
        print(self.frame_counter)
        if (self.frame_counter + 1) % 6 == 0:
            print("Reached 6 Frames")
            self.start(conf, runtime)
        else:
            # Go through each tracker to update the coordinates
            for i in range(10):

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
                elif self.car[i].coords[self.frame_counter-1][0] is not -1:
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
        self.frame_counter += 1

    # Updates car object with information for the car
    def update_car(self, n, coords, plate = None):
        self.car[n].coords[self.frame_counter] = coords

        if plate is not None:
            self.car[n].plate.append(plate)
        # print("Calculating deltas")
        # self.car[n].calculate_delta(self.counter-1)

    def processing(self, out):
        # for i in range(len(self.car)-1):
        #     self.final_plate[i] = mode(self.car[i].plate)
        self.run_count += 1
        for car in self.car:
            try:
                print("PLATES: ", car.plate)
                car.final_plate = mode(car.plate)
            except:
                print("mode function invalid")
                car.final_plate = 'halo'

        for i in range(self.frame_counter - 1):
            tempframe = pilEncrypt(self.car, self.frame[i], i)
            out.write(tempframe)

    # Converts the coordinates from (x1, y1, x2, y2) to (x, y, width, height)
    def convert_coords(self, coord):
        x = coord[0]['x']
        y = coord[0]['y']
        width = coord[2]['x'] - x
        height = coord[2]['y'] - y
        return x, y, width, height

    def frame_count(self):
        return self.frame_counter
