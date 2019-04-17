from Crypto.Cipher import Salsa20
from Crypto.Cipher import ChaCha20
from Crypto.Cipher import AES
from base64 import b64encode
import cv2


def set_salsa():
    key = b'1234567891234567'
    cipher = Salsa20.new(key)
    return cipher


def set_chacha(key):
    cipher = ChaCha20.new(key=key)
    return cipher


def encrypt_salsa(frame, cipher):

    data = cv2.imencode('.jpg', frame)[1].tostring()
#    data = str.encode(data)
    output = cipher.nonce + cipher.encrypt(data)
    return output


def encrypt_chacha(frame, cipher):
    data = cv2.imencode('.jpg', frame)[1].tostring()
#    data = str.encode(data)
    # nonce = b64encode(cipher.nonce).decode('utf-8')
    # print(data)
    output = cipher.nonce + cipher.encrypt(data)
    return output


def encrypt_AES(frame):
    key = "1234567891234567"
    key = str.encode(key)
    data = cv2.imencode('.jpg', frame)[1].tostring()
#    data = str.encode(data)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    output = cipher.nonce + tag + ciphertext
    return output
