
import cv2
import encrypt
import connection
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

    while ret:
        for i in range(300):
            ret, frame = cap.read()
            if ret is True:
                print(frame)
                # Encrypting frame
                output = encrypt.encrypt_chacha(frame, cipher)
                # adding ending terminator
                connection.send_message(len(output), s)
                # output = output + str.encode("halo")
                print("Sending frame " + str(i+1))
                connection.send_message(output, s)
            else:
                break
            i += 1

        ret = False


if __name__ == "__main__":
    main()
