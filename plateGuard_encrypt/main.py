from coordRetrv import *
from pilEncrypt import *
import json
# Temporary commented out
# from signalHandler import signal_handler
# import signal

def main():

    # reading from personal config file to get image location and alpr file locations
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    # This is kakka
    # signal.signal(signal.SIGSEGV,signal_handler)
    # Finds the plate and coordinates of the plate

    # running ALPR to get loaction/names of plates in picture
    results = coordRetrv(config['conf'], config['runtime'], config['image_location'])

    # Encrypts image and saves over original
    pilEncrypt(results, config['image_location'])

main()
