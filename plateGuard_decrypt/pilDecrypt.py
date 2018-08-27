# Import the modules
#from PIL import Image
import random
import cv2

# TODO


def pilDecrypt(plate, frame):

        # Load an image from the hard drive
        img = frame

        # license plate string to use as decrypt key
        lp = plate.upper()
        print(plate)

        # seed from ascii values of lp
        seed = 0
        for p in range(0, len(lp)):
            seed = seed + ord(lp[p])

        # getting num plates
        num_plates = img[0, 0, 0]

        # printing out image too encrypt with key
        # cv2.imshow('encrypted', img)
        # k = cv2.waitKey(0)

        # setting starting address to gather coord of plates(increased by 4 for each plate)
        j = 1

        # loop for gathering coords of plates from metadata
        for i in range(0, num_plates):

            # format img[x,y,[B:0,G:1,R:2]))
            # data = 1234, data1 = 12, data2 = 34. coord = str(data1 + data2)
            test = "test_frames/test"+str(i)+".png"
            cv2.imwrite(test, frame)
            x_data1 = str(img[0, j, 1])
            x_data2 = str(img[0, j, 0])
            x1 = int(str(x_data1 + x_data2.zfill(2)))

            y_data1 = str(img[0, j+1, 1])
            y_data2 = str(img[0, j+1, 0])
            y1 = int(str(y_data1 + y_data2.zfill(2)))

            x_data1 = str(img[0, j+2, 1])
            x_data2 = str(img[0, j+2, 0])
            x2 = int(str(x_data1 + x_data2.zfill(2)))

            y_data1 = str(img[0, j+3, 1])
            y_data2 = str(img[0, j+3, 0])
            y2 = int(str(y_data1 + y_data2.zfill(2)))

            j += 4

            print("Plate ", int(j/4), "coordinates")
            print("x1", x1)
            print("y1", y1)
            print("x2", x2)
            print("y2", y2, "\n")

            # getting sequence of rand according to lp input
            random.seed(seed)

            # decrypting plates
            # for x in range(x1, x2, ):
            #     for y in range(y1, y2, ):
            #         # getting bgr value of pixel
            #         b, g, r = img[y, x]
            #         # decrypting image
            #         img.itemset((y, x, 0), b ^ random.randint(1, 255))
            #         img.itemset((y, x, 1), g ^ random.randint(1, 255))
            #         img.itemset((y, x, 2), r ^ random.randint(1, 255))

        # Return the decrypted frame
        return frame
        # displaying decrypted image
        # cv2.imshow('unencrypted', img)
        # k = cv2.waitKey(0)






