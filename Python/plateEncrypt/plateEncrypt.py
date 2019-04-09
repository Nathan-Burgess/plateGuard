"""
Main program for plateEncrypt system
"""

import cv2
import buffer
import processing
import save
import glob
import os
import tracking
import dcounter

DEBUG = True


def main():

    if DEBUG:
        files = glob.glob("../20190401/0000/*")
        for f in files:
            os.remove(f)

    # TODO Change to pipe from ImageDecrypt
    # Read from file to import video
    cap = cv2.VideoCapture("../../test_plates/test_video3.mp4")
    # Something for writing out the video, codec related probably
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Set up output file
    out = cv2.VideoWriter('../20190401/0000/output.avi', fourcc, 30, (3840, 2160))

    track = tracking.Tracker()
    # Counter for number of frames
    j = 0
    # Return boolean to ensure reading in frames
    ret = True

    d_counter = dcounter.DCounter()

    # Loops through while video is reading in
    while ret:
        # Initialize buffer object
        buff = buffer.Buffer()
        buff.encrypt_path = "../20190401/0000/"
        # Read in frames
        print("Read in frames...")
        for i in range(60):
            ret, frame = cap.read()
            if ret is True:
                buff.frames.append(frame)
            else:
                break
        print("Finding Plates...")
        track.frame_counter = 0
        track.start(buff)
        for i in range(1, len(buff.frames)):
            track.update(buff, d_counter)
        buff.frame_num = j
        print("Encrypt License Plates...")
        processing.clear_plate_area(buff)
        j += 60
        print("Saving Buffer...")
        save.save_frame(buff, out)

    cap.release()
    out.release()


if __name__ == "__main__":
    main()
