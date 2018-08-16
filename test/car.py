# Holds the car data
import sys


class Car:

    def __init__(self):
        self.exists = []
        for i in range(600):
            self.exists.append(0)
        self.plate = []
        self.final_plate = ""
        self.coords = []
        self.delta_min = sys.maxsize
        self.delta_max = 0
        for i in range(600):
            self.coords.append((-1, -1, -1, -1))

    # Calculates the average delta between the current coordinates and the previous coordinates
    # def calculate_delta(self, frame_num):
    #     print("current coords: ", self.coords[frame_num])
    #     print("last coords: ", self.coords[frame_num-1])
    #     if self.coords[frame_num][0] == -1 or self.coords[frame_num-1][0] == -1:
    #         return
    #     d = abs(self.coords[frame_num][0] - self.coords[frame_num-1][0])
    #     d += abs(self.coords[frame_num][1] - self.coords[frame_num-1][1])
    #     d = d / 2
    #     print("delta: ",d)
    #
    #     if d < self.delta_min:
    #         self.delta_min = d
    #
    #     if d > self.delta_max:
    #         self.delta_max = d
