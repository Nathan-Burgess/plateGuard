import json
import sys
from pilDecrypt import *
import cv2


def main():
    if len(sys.argv) < 3:
        print("Usage: main.py <license plate> <image path>")
        sys.exit(1)

    # set up the video capture/writing
    cap = cv2.VideoCapture(sys.argv[2])
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 29.8, (1920,1080))

    ret = True

    while ret:
        # Read in the frames
        ret, frame = cap.read()

        if ret is True:
            frame = pilDecrypt(sys.argv[1], frame,)
            out.write(frame)

if __name__ == "__main__":
    main()