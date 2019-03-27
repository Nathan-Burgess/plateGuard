
from Crypto.Cipher import AES
import unittest
import save


# function to encrypt a string with a given key, or uses defualt
def encrypt(frame_num, car_num, string, key, path):

    # make the key 16 bytes long and convert into byte data
    key1 = (key * 16)[0:16]
    key = str.encode(key1)

    # performs 128 bit AES encryption with EAX modification dedication
    string1 = str.encode(string)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(string1)

    save.save_encypt(cipher.nonce, tag, ciphertext, frame_num, car_num, path)

    # return ciphertext, tag, cipher.nonce


class TestEncrypt(unittest.TestCase):
    def test_decrypt(self):
        bE = str.encode("This is a test string")
        ciphertext, tag, nonce = encrypt(bE, "halo")
        # file_i
        key1 = ("halo" * 16)[0:16]
        key = str.encode(key1)

        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data1 = cipher.decrypt_and_verify(ciphertext, tag)

        data = data1.decode()
        self.assertEqual("This is a test string", data)


if __name__ == "__main__":
    unittest.main()
