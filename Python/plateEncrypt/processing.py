"""
Manages processing of incoming frames, lp detection and encryption
"""

# import buffer
# import cv2
import detect
# import car as CAR
import random
import sys
import encrypt
import pickle
import tracking
from statistics import mode

DEBUG = True

# Calls openALPR and appends results to self.results
def call_detect(buff):
    # Gets results from openALPR
    for i in range(len(buff.frames)):
        result = detect.detect(buff.frames[i])
        if result:
            # Saves results to car per frame
            calculate_knn(buff, result, i)
            # Trackers.start(result)


# Blanks out license plate area after encrypting
def clear_plate_area(buff):
    for car in buff.cars:
        if car.plate:
            try:
                car.final_plate.append(mode(car.plate))
            except:
                car.final_plate.append("halo")
            print("After mode: " + str(car.final_plate))
        if car.final_plate is not "halo" and DEBUG:
            print("Final: " + car.final_plate)
    # Loop through all frames in buffer
    for i, frame in enumerate(buff.frames):
        # Loop through cars per frame
        for n, car in enumerate(buff.cars):
            strp = ""
            strc = ""
            data = {'coords': {}, 'pixel_data': [], 'frame': i+buff.frame_num}
            # Get (x1,y1), (x2,y2) coordinates for each plate area
            if car.coords[i] is not -1:
                print("In if " + str(car.final_plate))
                a, b, c, d = car.coords[i]
                data['coords'] = {'x1': a['x'], 'x2': c['x'], 'y1': a['y'], 'y2': c['y']}
                x1 = int(a['x'])
                x2 = int(c['x'])
                y1 = int(a['y'])
                y2 = int(c['y'])

                # Blank each plate to static
                for x in range(x1, x2):
                    for y in range(y1, y2):
                        b, g, r = frame[y, x]
                        strp = (b, g, r)
                        data['pixel_data'].append(strp)
                        frame.itemset((y, x, 0), random.randint(1, 255))
                        frame.itemset((y, x, 1), random.randint(1, 255))
                        frame.itemset((y, x, 2), random.randint(1, 255))

                bin_data = pickle.dumps(data)
                encrypt.encrypt(buff.frame_num + i, n, bin_data, car.final_plate[0].upper(), buff.encrypt_path)
            else:
                if car.coords[i-1] is not -1 and len(car.final_plate) > 1:
                    car.final_plate.pop(0)
                print("After potential pop: " + str(car.final_plate))


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