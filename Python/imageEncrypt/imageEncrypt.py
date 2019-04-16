import numpy as np

import cv2
import encrypt
from Crypto.Cipher import ChaCha20


def main():
    # Read from file to import video
    cap = cv2.VideoCapture("../../test_plates/test_video3.mp4")
    # Something for writing out the video, codec related probably
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Set up output file
    out = cv2.VideoWriter('../imageFiles/output.avi', fourcc, 30, (3840, 2160))

    ret = True
    # cipher = encrypt.set_salsa()
    cipher = encrypt.set_chacha()


    while ret:
        for i in range(1):
            ret, frame = cap.read()
            print(frame)
            cv2.imwrite("origional.jpg", frame)
            if ret is True:
               # encrypt.encrypt_salsa(frame, cipher)
               # encrypt.encrypt_AES(frame)
               output = encrypt.encrypt_chacha(frame, cipher)
            else:
                break

        print("Finding Plates...NOTTTTTTTT")
        key = b'12345678912345671234567891234567'
        nounce = output[:8]
        ciphertext = output[8:]
        cipher = ChaCha20.new(key=key, nonce=nounce)
        decoded = cipher.decrypt(ciphertext)
        #frame2 = cv2.imdecode(decoded, cv2.IMREAD_COLOR)
        frame2 = cv2.imdecode(np.frombuffer(decoded, np.uint8), -1)
        cv2.imwrite("decoded.jpg", frame2)
        print(frame2)
        ret = False


if __name__ == "__main__":
    main()
