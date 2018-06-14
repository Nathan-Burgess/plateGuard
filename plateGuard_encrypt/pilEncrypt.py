# Import the modules
#from PIL import Image
import random
import cv2

#TODO add number of plates and coords as metadata

def pilEncrypt(plate, image_location):

        # Load an image from the hard drive
        img = cv2.imread(image_location)

        #licsense plate string
        LP = plate['plate']
        # print(LP)

        # seed from asci values of LP
        seed = 0
        for p in range(0, len(LP)):
            seed = seed + ord(LP[p])

        #coordinates of top left and bottom right points
        coordinates = plate['coordinates']
        a = coordinates[0]
        b = coordinates[2]
        x1 = a['x']
        x2 = b['x']
        y1 = a['y']
        y2 = b['y']

        random.seed(seed)
        # print(seed)

        # Showing original unencrypted image
        cv2.imshow('Original', img)
        k = cv2.waitKey(0)

        # #encypting image plate
        for x in range(x1, x2, ):
            for y in range(y1, y2, ):
                # getting bgr value of pixel
                b, g, r = img[y,x]
                # encrpting image
                img.itemset((y, x, 0), b ^ random.randint(1, 255))
                img.itemset((y, x, 1), g ^ random.randint(1, 255))
                img.itemset((y, x, 2), r ^ random.randint(1, 255))

        # Display cords
        # print(x1)
        # print(y1)
        # print(x2)
        # print(y2)

        #Addying metadata to the image

        # #how many lisnce plates (#num of plates, 0, 0)
        num_plates = 1
        img.itemset((0, 0, 0), num_plates)

        x1_data = str(x1)

        if len(x1_data) == 3:
            img.itemset((0, 1, 0), int(str(x1_data[0] + x1_data[1])))
            img.itemset((0, 1, 1), int(str(x1_data[2])))
            img.itemset((0, 1, 2), 3)

        y1_data = str(y1)

        if len(y1_data) == 3:
            img.itemset((0, 2, 0), int(str(y1_data[0] + y1_data[1])))
            img.itemset((0, 2, 1), int(str(y1_data[2])))
            img.itemset((0, 2, 2), 3)

        x2_data = str(x2)

        if len(x2_data) == 3:
            img.itemset((0, 3, 0), int(str(x2_data[0] + x2_data[1])))
            img.itemset((0, 3, 1), int(str(x2_data[2])))
            img.itemset((0, 3, 2), 3)

        y2_data = str(y2)

        if len(y2_data) == 3:
            img.itemset((0, 4, 0), int(str(y2_data[0] + y2_data[1])))
            img.itemset((0, 4, 1), int(str(y2_data[2])))
            img.itemset((0, 4, 2), 3)



        print(x1_data)
        print(y1_data)
        print(x2_data)
        print(y2_data)



        # displaying ecrypted image
        cv2.imshow('Encrypted', img)
        k = cv2.waitKey(0)

        # saving image
        cv2.imwrite(image_location, img)
