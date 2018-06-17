import sys
from openalpr import Alpr
#import signal
#from signalHandler import signal_handler
#import time

# Retreives coordinates and license plate
def coordRetrv(conf, runtime, image_location):

    #configure ALPR setting according to config file
    alpr = Alpr("us", conf, runtime)

    # Tests if ALPR is able to open
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    # Gets the top result from ALPR for each plate
    alpr.set_top_n(1)
    alpr.set_default_region("md")

    # Loads results from the openALPR library
    results = alpr.recognize_file(image_location)

    result = results['results']

    # print(result)
    # Prints the number of license plates
    # print(len(result))

    # TODO: Figure out why this isnt working(maybe needs to be called at end of main
    #alpr.unload()

    # return list of all liscening plates in picture according to ALPR
    return result