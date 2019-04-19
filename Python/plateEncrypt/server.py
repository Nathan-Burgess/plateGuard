import socket
import numpy
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import buffer
import cv2


class Server:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.port = 3000

        self.sock.bind(('', self.port))
        self.sock.listen(1)
        self.end = 'halo'.encode()
        self.key = ""

    def handshake(self, client):
        halfkey = client.recv(16)
        print("Received partial key...")
        self.key = get_random_bytes(16)
        print("Built full key...")
        self.key = halfkey + self.key
        print("Sending key...")
        client.sendall(self.key)

    def receiveframes(self, client, buff):
        total_data = []
        data = ''

        while True:
            data = client.recv(8192)
            if self.end in data:
                total_data.append(data[:data.find(self.end)])
                break
            total_data.append(data)
            if len(total_data) > 1:
                # check if end_of_data was split
                last_pair = total_data[-2] + total_data[-1]
                if self.end in last_pair:
                    total_data[-2] = last_pair[:last_pair.find(self.end)]
                    total_data.pop()
                    break
        frame = total_data[0]
        for part in total_data[1:]:
            frame += part

        buff.encrypted_frames = frame

    def decryptframes(self, buff, i):
        frame = buff.encrypted_frames
        nounce = frame[:8]
        ciphertext = frame[8:]
        cipher = ChaCha20.new(key=self.key, nonce=nounce)
        decoded = cipher.decrypt(ciphertext)
        frame2 = cv2.imdecode(numpy.frombuffer(decoded, numpy.uint8), -1)
        print("Writing picture to file")
        outname = "decoded_" + i + ".jpg"
        cv2.imwrite(outname, frame2)
        buff.frames.append(frame2)


if __name__ == "__main__":
    s = Server()
    buff = buffer.Buffer()
    while True:
        print("Waiting for client")
        client, addr = s.sock.accept()
        print("Client connected from " + str(addr))
        s.handshake(client)
        for i in range(150):
            print("Receiving frame " + str(i+1))
            s.receiveframes(client, buff)
            # print("Writing picture to file...")
            # frame = buff.encrypted_frames[0]
            # print(frame)
            # cv2.imwrite("unencrypted.jpg", frame)
            print("Decrypting frame " + str(i+1))
            s.decryptframes(buff, i)
        client.close()