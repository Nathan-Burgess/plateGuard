import glob
import unittest
from Crypto.Cipher import AES


def print_decrypt(files, key):

    keys = key.encode()
    for file in files:


        file_in = open(file, "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

        # let's assume that the key is somehow available again
        cipher = AES.new(keys, AES.MODE_EAX, nonce)
        print(file)
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
            print(data)
        except ValueError:
            print("Invalid key")
