import json
import sys

with open("config.json", "r") as read_file:
    config = json.load(read_file)

if len(sys.argv) < 3:
    print("Usage: main.py <license plate> <image name>")
    sys.exit(1)

#TODO Add in the function call for decrypting, will take arguments: sys.arg[1] sys.arg[2]