import json
from coordRetrv import *
from statistics import mode
import cv2
from pilEncrypt import *

class buffer:

    # list of plate numbers
    plates = []
    # plate after finding mode
    final_plate = ''
    # list of frame objects
    frame = []
    # list of bbox objects
    coords = []

def main():

    buff = buffer()
    # Set up tracker.
    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE']
    tracker_type = tracker_types[2]
    tracker = cv2.TrackerKCF_create()

    #reading from json to run alpr
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    #opening video capture
    cap = cv2.VideoCapture(config['image_location'])
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 29.8, (1920, 1080))

    #running ALPR until a frame with a liscnce plate is found
    results = {}
    counter = -1

    while(len(results) == 0):
        ret, frame = cap.read()
        if ret == True:
            results = coordRetrv(config['conf'], config['runtime'], frame)
            counter += 1
            buff.frame.append(frame)
            bbox = (-1, -1, -1, -1)
            buff.coords.append(bbox)
        else:
            break

    # getting the coords of the liscnce plate and plate number
    for plate in results:
        coordinates = plate['coordinates']
        LP = plate['plate']
        # Store plate guess in buffer
        buff.plates.append(LP)
        a = coordinates[0]
        b = coordinates[2]
        x1 = a['x']
        x2 = b['x']
        y1 = a['y']
        y2 = b['y']
        break

    # Define an initial bounding box with coords of license plate
    bbox = (x1, y1, (x2-x1), (y2-y1))

    # Stores coordinates in the buffer
    buff.coords[counter] = bbox

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    # varible to track when to run ALPR every 6th frame it was last run
    track = 0

    # running for 60 frames
    for i in range(60):

        # Read a new frame
        ok, frame = cap.read()
        buff.frame.append(frame)
        if not ok:
            break

        # Start timer
        timer = cv2.getTickCount()

        # running ALPR since its been the 6th time since it ran
        if track == 6:

            # running ALPR until a frame with a lisnce plate is found
            results = {}
            while (len(results) == 0):
                ret, frame = cap.read()
                if ret == True:
                    results = coordRetrv(config['conf'], config['runtime'], frame)
                    counter += 1
                    buff.frame.append(frame)
                    bbox = (-1, -1, -1, -1)
                    buff.coords.append(bbox)
                else:
                    break
            print(results)

            #getting the coords of the plate and the plate_num
            for plate in results:
                LP = plate['plate']
                # adds to license plate list
                buff.plates.append(LP)
                coordinates = plate['coordinates']
                a = coordinates[0]
                b = coordinates[2]
                x1 = a['x']
                x2 = b['x']
                y1 = a['y']
                y2 = b['y']
                break

            # Define an initial bounding box
            bbox = (x1, y1, (x2 - x1), (y2 - y1))
            buff.coords[counter] = bbox

            # making new tracking object
            tracker = cv2.TrackerKCF_create()

            # Initialize tracker with first frame and bounding box
            ok = tracker.init(frame, bbox)
            track = 0


        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        # Checks if the tracker updated correctly, if so success, if not run ALPR and make new tracker
        if ok:
            print("SUCCESS")
            buff.coords[counter] = bbox
            # Tracking success
            #p1 = (int(bbox[0]), int(bbox[1]))
            #p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            #cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            #cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            print("TRACKING FAILED RUNNING ALPR AGAIN")

            #run ALPR until a frame with a liscnce plate is found
            results = {}
            while (len(results) == 0):
                ret, frame = cap.read()
                if ret == True:
                    results = coordRetrv(config['conf'], config['runtime'], frame)
                    counter += 1
                    buff.frame.append(frame)
                    bbox = (-1, -1, -1, -1)
                    buff.coords.append(bbox)
                else:
                    break
            print(results)

            #getting the coords and the plate_num
            for plate in results:
                LP = plate['plate']
                buff.plates.append(LP)
                coordinates = plate['coordinates']
                a = coordinates[0]
                b = coordinates[2]
                x1 = a['x']
                x2 = b['x']
                y1 = a['y']
                y2 = b['y']
                break

            # Define an initial bounding box and creating a new tracker
            bbox = (x1, y1, (x2 - x1), (y2 - y1))
            buff.coords[counter] = bbox
            tracker = cv2.TrackerKCF_create()

            # Initialize tracker with first frame and bounding box
            ok = tracker.init(frame, bbox)
            track = 0
            ok, bbox = tracker.update(frame)

        # printing the box location of the tracker
        print("PRINT BBOX" + str(bbox))
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display result
        cv2.imshow("Tracking", frame)
        track = track + 1

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    # printing the lisnce plates got and the mode
    print(buff.plates)
    buff.final_plate = mode(buff.plates)
    print(buff.final_plate)

    print(len(buff.coords))
    print(len(buff.frame))
    for i in range(60):
        tempframe = pilEncrypt(buff.final_plate, buff.frame[i], buff.coords[i])
        out.write(tempframe)

    sys.exit()

main()