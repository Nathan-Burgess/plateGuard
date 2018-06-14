import sys
from openalpr import Alpr
import signal
from signalHandler import signal_handler
import time

# Retreives coordinates and license plate
def coordRetrv(conf, runtime, image_location):
    alpr = Alpr("us", conf, runtime)

    # Tests if ALPR is able to open
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    # Checks for up to 20 plates
    alpr.set_top_n(20)
    alpr.set_default_region("md")

    # Loads results from the openALPR library
    results = alpr.recognize_file(image_location)

    result = results['results']

    # Prints the number of license plates
    print(len(result))

    plate = result[0]

   # alpr.unload()

    return plate