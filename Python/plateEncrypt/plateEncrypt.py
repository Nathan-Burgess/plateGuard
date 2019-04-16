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
import time

DEBUG = True


def main():

    if DEBUG:
        files = glob.glob("../20190401/0000/*")
        for f in files:
            os.remove(f)

    total_time = 0
    total_frames = 0

    # TODO Change to pipe from ImageDecrypt
    # Read from file to import video
    cap = cv2.VideoCapture("../../test_plates/test_video6.mp4")
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

    k = 0
    # Loops through while video is reading in
    while ret:
        # Initialize buffer object
        buff = buffer.Buffer()
        buff.encrypt_path = "../20190401/0000/"
        # Read in frames
        print("Read in frames...")
        for i in range(300):
            ret, frame = cap.read()

            if ret is True:
                buff.frames.append(frame)
            else:
                break
        d_counter.max = 1
        total_frames += i
        print("Finding Plates...")
        track.frame_counter = 0
        start = time.time()
        track.start(buff, d_counter)
        for i in range(1, len(buff.frames)):
            track.update(buff, d_counter)
        buff.frame_num = j
        total_time += (time.time() - start)

        print("Encrypt License Plates...")
        processing.clear_plate_area(buff)
        j += 300
        print("Saving Buffer...")
        save.save_frame(buff, out)
        buff.frames.clear()
        k += 1
        if k is 6:
            break

    cap.release()
    out.release()

    print("Average Time Per Frame: " + str(total_time/total_frames))



if __name__ == "__main__":
    main()
