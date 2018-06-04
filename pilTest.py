# Import the modules
from PIL import Image
import random

try:

    # Load an image from the hard drive
    original = Image.open("C:/Users/natha/Desktop/car_plate.jpg")

    # loading pixel values
    pixels = original.load()

    #licsense plate string
    test = 'slgbg'

    # seed from asci values of LP
    seed = 0
    for p in range(0, len(test)):
        seed = seed + ord(test[p])

    #coordinates of top left and bottom right points
    x1 = 1424
    x2 = 1961
    y1 = 1399
    y2 = 1644

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





except:
    print("Error somewhere")
