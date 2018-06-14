from coordRetrv import *
from pilEncrypt import *
import json
from signalHandler import signal_handler
import signal

def main():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

   # signal.signal(signal.SIGSEGV,signal_handler)
    # Finds the plate and coordinates of the plate
    results = coordRetrv(config['conf'], config['runtime'], config['image_location'])

    # Encrypts and then decrpyts the plate
    pilEncrypt(results, config['image_location'])

main()
