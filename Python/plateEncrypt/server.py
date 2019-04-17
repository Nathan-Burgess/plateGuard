import socket
from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes


class Server:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.hostname = socket.gethostname()
        self.port = 3000

        self.sock.bind((self.hostname, self.port))
        self.sock.listen(1)

    def handshake(self, client):
        halfkey = client.recv(16)
        print("Received partial key...")
        key = get_random_bytes(16)
        print("Built full key...")
        key += halfkey
        print("Sending key...")
        client.sendall(key)

    def receiveframes(self, buff):
        return

    def decryptframes(self, buff):
        return


if __name__ == "__main__":
    s = Server()
    while True:
        print("Waiting for client")
        client, addr = s.sock.accept()
        print("Client connected from " + str(addr))
        s.handshake(client)
