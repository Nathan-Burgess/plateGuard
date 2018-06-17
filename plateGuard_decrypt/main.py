import json
import sys
from pilDecrypt import *

# reading from personal config file to get LP to decrypt and image location
with open("config.json", "r") as read_file:
    config = json.load(read_file)

if len(sys.argv) < 3:
    print("Usage: main.py <license plate> <image name>")
    sys.exit(1)

# run decrypt to run decryption on plates according to the LP provided
pilDecrypt(sys.argv[1], sys.argv[2], config['image_location'])