"""
Runs openalpr to detect license plate number for cars
"""

import sys
from openalpr import Alpr


def detect(frame):
    # Configure ALPR setting according to config file
    alpr = Alpr("us", "/usr/share/openalpr/config/openalpr.defaults.conf", "/usr/share/openalpr/runtime_data/")

    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    # Get the top result from ALPR for each plate
    alpr.set_top_n(1)
    alpr.set_default_region("tx")

    # Loads results from the openALPR library
    results = alpr.recognize_ndarray(frame)
    result = results['results']

    return result
