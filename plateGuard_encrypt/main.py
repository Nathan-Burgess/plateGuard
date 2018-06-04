from plateGuard_encrypt.coordRetrv import *
from plateGuard_encrypt.pilEncrypt import *
import json

with open("config.json", "r") as read_file:
    config = json.load(read_file)

# Finds the plate and coordinates of the plate
plate = coordRetrv(config['conf'], config['runtime'], config['image_location'])

# Encrypts and then decrpyts the plate
pilEncrypt(plate, config['image_location'])