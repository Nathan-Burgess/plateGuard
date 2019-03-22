"""
Main program for plateEncrypt system
"""

import cv2
import json
import buffer
import processing
from detect import detect


def main():
    # Read from config file
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    # TODO Change to pipe from ImageDecrypt
    # Read from file to import video
    cap = cv2.VideoCapture("../../test_plates/")
    # Something for writing out the video, codec related probably
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Set up output file
    out = cv2.VideoWriter('output.avi', fourcc, 29.8, (1920,1080))

    # Counter for number of frames
    j = 0
    # Return boolean to ensure reading in frames
    ret = True


    # Loops through while video is reading in
    while ret:
        # Initialize buffer object
        buff = buffer.Buffer()

        # Read in frames
        for i in range(60):
            ret, frame = cap.read()

            if ret is True:
                buff.frame.append(frame)
            else:
                break

        proc = processing.Processing(buff, out)

    cap.release()
    out.release()


if __name__ == "__main__":
    main()
