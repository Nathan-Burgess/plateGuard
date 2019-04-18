import numpy as np

import cv2
import encrypt
import connection
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

def main():
    # Read from file to import video
    cap = cv2.VideoCapture("../../test_plates/test_video3.mp4")
    # Something for writing out the video, codec related probably
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Set up output file
    out = cv2.VideoWriter('../imageFiles/output.avi', fourcc, 30, (3840, 2160))

    s = connection.start_connection()
    host_ip = connection.connect_to_host("vmware.cse.unt.edu", 3000, s)
    print("the socket has successfully connected")

    key = get_random_bytes(16)
    print(key)
    connection.send_message(key, s)

    key = connection.recv_message(32, s)
    print(key)

    ret = True
    # cipher = encrypt.set_salsa()
    cipher = encrypt.set_chacha(key)


    while ret:
        for i in range(300):
            ret, frame = cap.read()
            print(frame)
            cv2.imwrite("origional.jpg", frame)
            if ret is True:
               # encrypt.encrypt_salsa(frame, cipher)
               # encrypt.encrypt_AES(frame)
                data = cv2.imencode('.jpg', frame)[1].tostring()
                data = data + str.encode("halo")
                output = encrypt.encrypt_chacha(frame, cipher)
                output = output + str.encode("halo")
                connection.send_message(output, s)
            else:
                break

        print("Finding Plates...NOTTTTTTTT")
       # nounce = output[:8]
       # ciphertext = output[8:]
       # cipher = ChaCha20.new(key=key, nonce=nounce)
       # decoded = cipher.decrypt(ciphertext)
        #frame2 = cv2.imdecode(decoded, cv2.IMREAD_COLOR)
        #frame2 = cv2.imdecode(np.frombuffer(data, np.uint8), -1)
        #cv2.imwrite("deco2ded.jpg", frame2)
        #print(frame2)
        print(data)
        ret = False


if __name__ == "__main__":
    main()
