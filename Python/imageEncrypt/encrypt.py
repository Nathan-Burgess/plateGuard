
from Crypto.Cipher import ChaCha20
import cv2


#sets up the cipher with given key
def set_chacha(key):
    cipher = ChaCha20.new(key=key)
    return cipher


#encypts the frame with given cipher, returns encypted string of bytes
def encrypt_chacha(frame, cipher,i):
    data = cv2.imencode('.jpg', frame)
    data = data[1].tobytes()
    # filename = "unecnrypted" + str(i)
    # f = open(filename, "w")
    # f.write(str(data))
    # f.close()
    # output = cipher.nonce + cipher.encrypt(data)
    output = data
    return output

