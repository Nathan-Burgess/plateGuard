# Import the modules
#from PIL import Image
import random
import cv2

#TODO add number of plates and coords as metadata

def pilEncrypt(results, image_location):

        # Load an image from the hard drive
        img = cv2.imread(image_location)

        # Showing original unencrypted image
        cv2.imshow('Original', img)
        k = cv2.waitKey(0)

        # Adding number of plates meta data to image

        # how many license plates (#num of plates, 0, 0)
        num_plates = len(results)
        # itemset((x, y, [B:0,G:1,R:2]), [new_value])
        img.itemset((0, 0, 0), num_plates)

        i = 1

        for plate in results:
            #licsense plate string
            LP = plate['plate']
            print(LP)

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

            # #encypting image plate
            for x in range(x1, x2, ):
                for y in range(y1, y2, ):
                    # getting bgr value of pixel
                    b, g, r = img[y, x]
                    # encrypting image
                    img.itemset((y, x, 0), b ^ random.randint(1, 255))
                    img.itemset((y, x, 1), g ^ random.randint(1, 255))
                    img.itemset((y, x, 2), r ^ random.randint(1, 255))

            # Adding coordinate metadata to the image

            # Sets metadata for x1
            img.itemset((0, i, 0), int(x1%100))
            img.itemset((0, i, 1), int(x1/100))

            # Sets metadata for y1
            img.itemset((0, i+1, 0), int(y1%100))
            img.itemset((0, i+1, 1), int(y1/100))

            # Sets metadata for x2
            img.itemset((0, i+2, 0), int(x2%100))
            img.itemset((0, i+2, 1), int(x2/100))

            # Sets metadata for y2
            img.itemset((0, i+3, 0), int(y2%100))
            img.itemset((0, i+3, 1), int(y2/100))

            i += 4

            # Display cords
            print(x1)
            print(y1)
            print(x2)
            print(y2)

        # displaying ecrypted image
        cv2.imshow('Encrypted', img)
        k = cv2.waitKey(0)

        # saving image
        cv2.imwrite(image_location, img)
