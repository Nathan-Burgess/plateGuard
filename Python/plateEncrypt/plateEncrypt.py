"""
Main program for plateEncrypt system
"""

import cv2
import numpy

import buffer
import processing
import save
import glob
import os
import tracking
import dcounter
import time
import server

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
    cap = cv2.VideoCapture("../../test_plates/sdd_test.mp4")
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
    # Initialize buffer object
    buff = buffer.Buffer()
    buff.encrypt_path = "../20190401/0000/"
    # Read in frames
    print("Read in frames...")
    s = server.Server()
    buff = buffer.Buffer()
    while ret:
        # print("Waiting for client")
        # client, addr = s.sock.accept()
        # print("Client connected from " + str(addr))
        # s.handshake(client)
        # for i in range(60):
        #     for j in range(5):
        #         print("Receiving frame " + str(i + j))
        #         s.recv_msg(client, buff)
        #         print("Received frame " + str(i+j))
        #         print("Writing frame " + str(i + j))
        #     client.sendall("halo".encode())
        # client.close()

        #
        # for i in range(len(buff.encrypted_frames)):
        #     decoded = buff.encrypted_frames[i]
        #     decoded_frame = cv2.imdecode(numpy.frombuffer(decoded, numpy.uint8), -1)
        #     outname = "decoded_" + str(i + 1) + ".jpg"
        #     try:
        #         print("Decoded_frame size: " + str(len(decoded_frame)))
        #         cv2.imwrite(outname, decoded_frame)
        #         buff.frames.append(decoded_frame)
        #     except TypeError:
        #         print("Errored")
        # print("Writing picture to file...")
        # frame = buff.encrypted_frames[0]
        # print(frame)
        # cv2.imwrite("unencrypted.jpg", frame)
        # print("Decrypting frame " + str(i + 1))
        # s.decryptframes(buff, i)

        print("Read in frames...")
        for i in range(300):
            ret, frame = cap.read()

            if ret is True:
                buff.frames.append(frame)
            else:
                break

        d_counter.max = 1
        total_frames += i
        print(len(buff.frames))
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

    cap.release()
    out.release()

    print("Average Time Per Frame: " + str(total_time/total_frames))


if __name__ == "__main__":
    main()
