'''
Holds car and frame objects
'''

import car

class Buffer:

    def __init__(self):
        self.cars = []
        self.frames = []
        for i in range(60):
            self.cars.append(car.Car())

if __name__ == "__main__":
    buf = Buffer()
    buf.test()