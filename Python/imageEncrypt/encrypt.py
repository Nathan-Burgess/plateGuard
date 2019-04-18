
from Crypto.Cipher import ChaCha20
import cv2


#sets up the cipher with given key
def set_chacha(key):
    cipher = ChaCha20.new(key=key)
    return cipher


#encypts the frame with given cipher, returns encypted string of bytes
def encrypt_chacha(frame, cipher):
    data = cv2.imencode('.jpg', frame)[1].tostring()
    output = cipher.nonce + cipher.encrypt(data)
    return output

