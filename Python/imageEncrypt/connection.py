import socket
import sys

#Sets up a TCP socket
def start_connection():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
    except socket.error as err:
        print("socket creation failed %s" % (err))
        sys.exit()

    return s

#connects to a host with given hostname and port, returns ip address of host
def connect_to_host(host_name, port, s):
    try:
        host_ip = socket.gethostbyname(host_name)
    except socket.gaierror:
        print("could not resolve host")
        sys.exit()

    s.connect((host_ip, port))

    return host_ip


#sends a message
def send_message(message, s):

    s.sendall(message)


#recives a message with given bytes
def recv_message(bytes, s):

    return s.recv(bytes)

