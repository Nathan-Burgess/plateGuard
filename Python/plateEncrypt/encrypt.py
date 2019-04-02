
from Crypto.Cipher import AES
import unittest
import save


# function to encrypt a string with a given key, or uses defualt
def encrypt(frame_num, car_num, data, key, path):

    # make the key 16 bytes long and convert into byte data
    key1 = (key * 16)[0:16]
    key = str.encode(key1)

    # performs 128 bit AES encryption with EAX modification dedication
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    save.save_encypt(cipher.nonce, tag, ciphertext, frame_num, car_num, path)


