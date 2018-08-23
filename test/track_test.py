
import json
from coordRetrv import *
from statistics import mode
import cv2
from pilEncrypt import *
from buffer import *
from Log import *

log = Log()

def main():
    # read from config file
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    # Set up the video capture/writing
    cap = cv2.VideoCapture(config['image_location'])
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 29.8, (1920, 1080))
    j = 0
    ret = True

    while ret:
        # Read in the frames

        buff = Buffer(j)
        j += 59

        ret, frame = cap.read()

        if ret is True:
            log.add_mult(1)
            buff.update_frame(frame)
            buff.start(config['conf'], config['runtime'])

            for i in range(1, 59):
                ret, frame = cap.read()
                if ret is True:
                    buff.update_frame(frame)
                    buff.update(config['conf'], config['runtime'])
                else:
                    break


        buff.processing(out)

    cap.release()
    out.release()


if __name__ == "__main__":
    main()
