
import cv2
import encrypt
import connection
import pickle
import struct
from Crypto.Random import get_random_bytes


def main():
    # Read from file to import video
    cap = cv2.VideoCapture("../../test_plates/test_video3.mp4")

    # Setting up Socket connection to server
    s = connection.start_connection()
    host_ip = connection.connect_to_host("vmware.cse.unt.edu", 3000, s)

    print("the socket has successfully connected")

    # generating halof of the cipher key
    key = get_random_bytes(16)

    # sending half of key to server
    connection.send_message(key, s)

    # receiving full key
    key = connection.recv_message(32, s)

    print(key)
    ret = True

    # Setting up cipher with correct key
    cipher = encrypt.set_chacha(key)

    count = 0
    while ret:
        for i in range(1, 301):
            ret, frame = cap.read()
            if ret is True:
                # print(frame)
                # Encrypting frame
                output = encrypt.encrypt_chacha(frame, cipher, i)
                # adding ending terminator
                output = output + str.encode("halo")
                print("Sending frame " + str(i+1))
                data = pickle.dumps(frame)

                # Send message length first
                message_size = struct.pack("L", len(data))  ### CHANGED

                # Then data
                s.sendall(message_size + data)
                # connection.send_message(output, s)
                print(len(output))

                if i % 5 == 0:
                    msg = s.recv(4)
            else:
                break


        ret = False


if __name__ == "__main__":
    main()
