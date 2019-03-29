import unittest
import cv2
import buffer
import processing
import detect
import sys
import encrypt
from Crypto.Cipher import AES
import save


class TestProcessing(unittest.TestCase):

    def test_call_detect(self):
        # Read from video, just one frame to test
        cap = cv2.VideoCapture("../../../test_plates/test_video_short.mp4")
        ret, frame = cap.read()
        self.assertTrue(ret)

        buff = buffer.Buffer()

        buff.frames.append(frame)

        processing.call_detect(buff)
        plate = buff.cars[0].plate

        self.assertTrue(plate)

    def test_clear_plate_area(self):
        # Read from video, just one frame to test
        cap = cv2.VideoCapture("../../../test_plates/test_video_short.mp4")
        ret, frame = cap.read()
        self.assertTrue(ret)

        buff = buffer.Buffer()

        buff.frames.append(frame)

        processing.call_detect(buff)

        processing.clear_plate_area(buff)
        cv2.imwrite("test_picture.jpg", buff.frames[0])


class TestDetect(unittest.TestCase):
    def test_detect_license_plate(self):
        image_location = "../../../test_plates/backup/ea7the.jpg"

        frame = cv2.imread(image_location)

        if frame is None:
            print("Error loading image")
            sys.exit(1)

        results = detect.detect(frame)

        self.assertTrue(results)


class TestEncrypt(unittest.TestCase):
    def test_decrypt_wrong_key(self):
        bE = str.encode("This is a test string")
        key1 = ('halo' * 16)[0:16]
        key = str.encode(key1)

        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(bE)
        key1 = ("halo1" * 16)[0:16]
        key = str.encode(key1)

        cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
        try:
            data1 = cipher.decrypt_and_verify(ciphertext, tag)
            data = data1.decode()
        except:
            check = True

        self.assertTrue(check)


if __name__ == "__main__":
    unittest.main()