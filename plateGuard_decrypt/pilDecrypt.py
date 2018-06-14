# Import the modules
#from PIL import Image
import random
import cv2

#pass in the liscence plate string

#TODO retreive plate coords from metadata

def pilDecrypt(plate, image_location, save_location):

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

        cv2.imshow('encrypted', img)
        k = cv2.waitKey(0)

        j = 1
        for i in range(0, num_plates):

            # x_data.append(img[0, 1, 0])
            x_data1 = str(img[0, j, 1])
            x_data2 = str(img[0, j, 0])
            # x_data.append(int(str(x_data1 + x_data2)))
            x1 = int(str(x_data1 + x_data2.zfill(2)))

            y_data1 = str(img[0, j+1, 1])
            y_data2 = str(img[0, j+1, 0])
            #y_data.append(int(str(y_data1 + y_data2)))
            y1 = int(str(y_data1 + y_data2.zfill(2)))

            x_data1 = str(img[0, j+2, 1])
            x_data2 = str(img[0, j+2, 0])
            #x_data.append(int(str(x_data1 + x_data2)))
            x2 = int(str(x_data1 + x_data2.zfill(2)))

            y_data1 = str(img[0, j+3, 1])
            y_data2 = str(img[0, j+3, 0])
            #y_data.append(int(str(y_data1 + y_data2)))
            y2 = int(str(y_data1 + y_data2.zfill(2)))

            j += 4
            # coords.append((x_data[0], y_data[0]), (x_data[1], y_data[1]))

            print(x1)
            print(y1)
            print(x2)
            print(y2)

            random.seed(seed)

            # unencrypting plate number
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





