# Holds the car data

class Car:

    def __init__(self):
        self.exists = []
        for i in range(60):
            self.exists.append(0)
        self.plate = []
        self.coords = []
        for i in range(60):
            self.coords.append((-1, -1, -1, -1))