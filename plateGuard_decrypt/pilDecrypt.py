# Import the modules
from PIL import Image
import random
import cv2

#pass in the liscence plate string

#TODO retreive plate coords from metadata

def pilDecrypt(plate, image_location):

        # Load an image from the hard drive
        #original = Image.open(image_location)
        img = cv2.imread(image_location)

        #licsense plate string
        LP = plate.upper()
        print(plate)

        # seed from asci values of LP
        seed = 0
        for p in range(0, len(LP)):
            seed = seed + ord(LP[p])

        #getting num plates
        num_plates = img[0, 0, 0]

        #coords = [(0, 0), (0, 0)]

        if num_plates == 1:


            x1_type = img[0, 1, 2]
            if x1_type == 3:
                #x_data.append(img[0, 1, 0])
                x_data1 = str(img[0, 1, 0])
                x_data2 = str(img[0, 1, 1])
             #   x_data.append(int(str(x_data1 + x_data2)))
                x1 = int(str(x_data1 + x_data2))
            y1_type = img[0, 2, 2]

            if y1_type == 3:
                y_data1 = str(img[0, 2, 0])
                y_data2 = str(img[0, 2, 1])
                #y_data.append(int(str(y_data1 + y_data2)))
                y1 = int(str(y_data1 + y_data2))

            x2_type = img[0, 3, 2]
            if x2_type == 3:
                x_data1 = str(img[0, 3, 0])
                x_data2 = str(img[0, 3, 1])
                #x_data.append(int(str(x_data1 + x_data2)))
                x2 = int(str(x_data1 + x_data2))

            y2_type = img[0, 4, 2]
            if y2_type == 3:
                y_data1 = str(img[0, 4, 0])
                y_data2 = str(img[0, 4, 1])
                #y_data.append(int(str(y_data1 + y_data2)))
                y2 = int(str(y_data1 + y_data2))

           # coords.append((x_data[0], y_data[0]), (x_data[1], y_data[1]))



        # x1 = 316
        # y1 = 140
        # x2 = 464
        # y2 = 203

        print(x1)
        print(y1)
        print(x2)
        print(y2)

        random.seed(seed)


        cv2.imshow('encrypted', img)
        k = cv2.waitKey(0)

        #unencrypting plate number
        # for x in range(coords[0, 0], coords[1, 0], ):
        #     for y in range(coords[0, 1], coords[1, 1], ):

        for x in range(x1, x2, ):
            for y in range(y1, y2, ):
                # getting bgr value of pixel
                b, g, r = img[y, x]
                # decrypting image
                img.itemset((y, x, 0), b ^ random.randint(1, 255))
                img.itemset((y, x, 1), g ^ random.randint(1, 255))
                img.itemset((y, x, 2), r ^ random.randint(1, 255))


        # displaying unecrypted image
        cv2.imshow('unencrypted', img)
        k = cv2.waitKey(0)


