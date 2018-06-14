import json
import sys
from pilDecrypt import *

with open("config.json", "r") as read_file:
    config = json.load(read_file)

if len(sys.argv) < 3:
    print("Usage: main.py <license plate> <image name>")
    sys.exit(1)

pilDecrypt(sys.argv[1], sys.argv[2])