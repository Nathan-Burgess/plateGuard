import socket
import numpy
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import buffer
import cv2
import struct
import pysnooper


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

    # @pysnooper.snoop()
    def recv_msg(self, client, buff):
        # BUFF_SIZE = 4096  # 4 KiB
        # data = b''
        #
        # while True:
        #     part = client.recv(BUFF_SIZE)
        #     data += part
        #     if len(part) < BUFF_SIZE:
        #         # either 0 or end of data
        #         break
        # return data

        total_data = []

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

        buff.encrypted_frames.append(frame)

    # @pysnooper.snoop()
    def receiveframes(self, client, n):
        data = b''

        while len(data) < n:
            # print("In while...")
            print(str(n) + " " + str(len(data)))
            packet = client.recv(n - len(data))
            if not packet:
                return None
            data += packet
            # print("Data += packet")
        return data

        # while True:
        #     data = client.recv(8192)
        #     if self.end in data:
        #         total_data.append(data[:data.find(self.end)])
        #         break
        #     total_data.append(data)
        #     if len(total_data) > 1:
        #         # check if end_of_data was split
        #         last_pair = total_data[-2] + total_data[-1]
        #         if self.end in last_pair:
        #             total_data[-2] = last_pair[:last_pair.find(self.end)]
        #             total_data.pop()
        #             break
        #
        # frame = total_data[0]
        # for part in total_data[1:]:
        #     frame += part

        # print("Frame size: " + str(len(frame)))
        # print(frame)
        # buff.encrypted_frames.append(frame)

    # @pysnooper.snoop()
    def decryptframes(self, buff, i):
        # frame = buff.encrypted_frames[-1]
        filename = "decrypted_out" + str(i)
        f = open(filename, "w")
        data = buff.encrypted_frames[i]
        nounce = data[:8]
        print(len(nounce))
        ciphertext = data[8:]
        cipher = ChaCha20.new(key=self.key, nonce=nounce)
        decoded = cipher.decrypt(ciphertext)
        f.write(str(decoded))
        f.close()
        print("Decoded size " + str(len(decoded)))
        decoded_frame = cv2.imdecode(numpy.frombuffer(decoded, numpy.uint8), -1)
        outname = "decoded_" + str(i+1) + ".jpg"
        print("Decoded_frame size: " + str(len(decoded_frame)))
        cv2.imwrite(outname, decoded_frame)
        buff.frames.append(decoded_frame)


if __name__ == "__main__":
    s = Server()
    buff = buffer.Buffer()
    while True:
        print("Waiting for client")
        client, addr = s.sock.accept()
        print("Client connected from " + str(addr))
        s.handshake(client)
        for i in range(20):
            s.recv_msg(client, buff)
            print("Received frame " + str(i+1))
            # print("Writing picture to file...")
            # frame = buff.encrypted_frames[0]
            # print(frame)
            # cv2.imwrite("unencrypted.jpg", frame)
        for i in range(20):
            print("Decrypting frame " + str(i+1))
            s.decryptframes(buff, i)
            # s.decryptframes(data, buff)
        client.sendall("halo".encode())
        client.close()
