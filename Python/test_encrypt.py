from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt():
    key = str.encode("1234567890123456")
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(str.encode("TEST TEST TEST"))

    file_out = open("encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

def decrypt():
    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    key = str.encode("1234567890123456")

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    print(data.decode())

if __name__ == "__main__":
    encrypt()
    decrypt()