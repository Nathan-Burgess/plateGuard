import sys
from openalpr import Alpr


# Retreives coordinates and license plate
def coord_retrv():
    alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "/home/michael/openalpr/runtime_data")

    # Tests if ALPR is able to open
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    # Checks for up to 20 plates
    alpr.set_top_n(20)
    alpr.set_default_region("md")

    # Loads results from the openALPR library
    results = alpr.recognize_file("/home/michael/Pictures/test_plates/ea7the.jpg")

    plate = results['results']

    alpr.unload()

    return plate