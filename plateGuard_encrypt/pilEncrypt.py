# Import the modules
from PIL import Image
import random


def pilEncrypt(plate, image_location):
    #try:

        # Load an image from the hard drive
        original = Image.open(image_location)

        # loading pixel values
        pixels = original.load()

        #licsense plate string
        LP = plate['plate']


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

        original.show()

        #encypting image plate
        for x in range(x1, x2, ):
            for y in range(y1, y2, ):
                r, g, b = original.getpixel((x, y))
                pixels[x, y] = ((r ^ random.randint(1, 255)), (g ^ random.randint(1, 255)), (b ^ random.randint(1, 255)))

        # Display encrypted
        original.show()

        #reseding using seed value
        random.seed(seed)

        #unencrypting plate number
        for x in range(x1, x2, ):
            for y in range(y1, y2, ):
                r, g, b = original.getpixel((x, y))
                pixels[x, y] = ((r ^ random.randint(1, 255)), (g ^ random.randint(1, 255)), (b ^ random.randint(1, 255)))


        ##displaying unecrypted image
        original.show()

        original.save(image_location)




    # except:
    #     print("Error somewhere")
