'''
Holds car and frame objects
'''

import car


class Buffer:

    def __init__(self):
        self.cars = [car.Car() for i in range(10)]
        self.frames = []
        self.frame_num = 0
        self.encrypt_path = ""
        self.encrypted_frames = None
