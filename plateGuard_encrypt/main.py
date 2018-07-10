from coordRetrv import *
from pilEncrypt import *
import json
import cv2 as cv
# Temporary commented out
# from signalHandler import signal_handler
# import signal

def main():

    # reading from personal config file to get image location and alpr file locations
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    cap = cv.VideoCapture(config['image_location'])
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 29.8, (1920, 1080))

    while(cap.isOpened()):
        ret, frame = cap.read()

        # running ALPR to get loaction/names of plates in picture
        results = coordRetrv(config['conf'], config['runtime'], frame)

        # Encrypts image and saves over original
        frame = pilEncrypt(results, frame)

        out.write(frame)

    cap.release()
    out.release()

main()
