#
#
#
#PROOF OF CONCEPT STUFF
#
#
#
#

import sys

from openalpr import Alpr

alpr = Alpr("us", "/etc/openalpr/openaplr.conf", "/home/michael/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("md")

results = alpr.recognize_file("/home/michael/Pictures/test_plates/ea7the.jpg")

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Coordinates"))
    print("   %12s %12s" % (plate['plate'], plate['coordinates']))
        # print(" %12s" % (results['coordinates']))

coordinates = plate['coordinates']

print(coordinates[0])
print(coordinates[2])

alpr.unload()