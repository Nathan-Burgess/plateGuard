import glob
import unittest
from Crypto.Cipher import AES
import pickle


def print_decrypt(files, key):

    FRAMES = []
    keys = key.encode()
    for file in files:

        file_in = open(file, "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

        # let's assume that the key is somehow available again
        cipher = AES.new(keys, AES.MODE_EAX, nonce)
        # print(file)
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
            data = pickle.loads(data)
            FRAMES.append(data)
            # print(data)
        except ValueError:
            pass

    return FRAMES


def decrypt_frame(data, frame):

    # for b, g, r in data['pixel_data']:
    x1 = data['coords']['x1']
    x2 = data['coords']['x2']
    y1 = data['coords']['y1']
    y2 = data['coords']['y2']

    a = 0
    for x in range(int(x1), int(x2)):
        for y in range(int(y1), int(y2)):
            b,g,r  = data["pixel_data"][a]
            frame.itemset((y, x, 0), b)
            frame.itemset((y, x, 1), g)
            frame.itemset((y, x, 2), r)
            a = a + 1

    return frame
