
import cv2
import detect
import processing


class Tracker:
    def __init__(self):
        self.tracker = []
        self.bbox = [(-1, -1, -1, -1) for i in range(10)]
        self.length = {'old': 0, 'new': 0}
        self.frame_counter = 0

    def start(self, buff):
        # Calls openalpr and receives results
        results = detect.detect(buff.frames[self.frame_counter])
        # Calculates KNN or initializes car objects
        processing.calculate_knn(buff, results, self.frame_counter)

        # Set up trackers
        self.tracker = [cv2.TrackerKCF_create() for i in range(10)]

        # Initialize bbox variables
        for i, car in enumerate(buff.cars):
            if car.coords[self.frame_counter] is not -1:
                self.bbox[i] = self.convert_to_hw(car.coords[self.frame_counter])
                self.tracker[i].init(buff.frames[self.frame_counter], self.bbox[i])
        self.update(buff)

    def update(self, buff):
        self.frame_counter += 1
        ok = True

        if self.frame_counter >= 60:
            return

        while ok:
            for i, tracker in enumerate(self.tracker):
                # Updates bbox
                ok, self.bbox[i] = tracker.update(buff.frames[self.frame_counter])

                # Update coordinates on car
                if ok:
                    buff.cars[i].coords[self.frame_counter] = self.convert_to_xy(self.bbox[i])
            if self.frame_counter >= 60:
                return
            self.frame_counter += 1

        if buff.cars[i].coords[self.frame_counter-2] is not -1:
            print("Lost Tracker")
            self.start(buff)
        else:
            self.update(buff)

    def convert_to_hw(self, coords):
        x = coords[0]['x']
        y = coords[0]['y']
        width = coords[2]['x'] - x
        height = coords[2]['y'] - y

        return x, y, width, height

    def convert_to_xy(self, coords):
        a = {'x': coords[0], 'y': coords[1]}
        b = {'x': coords[0]+coords[2], 'y': coords[1]}
        c = {'x': coords[0]+coords[2], 'y': coords[1]+coords[3]}
        d = {'x': coords[0], 'y': coords[1]+coords[3]}

        return a, b, c, d
