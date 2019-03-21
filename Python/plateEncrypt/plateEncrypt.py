"""
Main program for plateEncrypt system
"""

import cv2
import json
from detect import detect


def main():
    # Read from config file
    with open("config.json", "r") as read_file:
        config = json.load(read_file)



if __name__ == "__main__":
    main()
