import socket
import sys


def start_connection():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
    except socket.error as err:
        print("socket creation failed %s" % (err))
        sys.exit()

    return s


def connect_to_host(host_name, port, s):
    try:
        host_ip = socket.gethostbyname(host_name)
    except socket.gaierror:
        print("could not resolve host")
        sys.exit()

    s.connect((host_ip, port))

    return host_ip


def send_message(message, s):

    s.sendall(message)
