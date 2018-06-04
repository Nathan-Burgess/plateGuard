# Import the modules
from PIL import Image, ImageFilter

try:
    # Load an image from the hard drive
    original = Image.open("C:/Users/natha/Desktop/car_plate.jpg")
    pixels = original.load()
    test = 'slgbg'

    x1 = 1424
    x2 = 1961
    y1 = 1399
    y2 = 1644


    # Blur the image
    blurred = original.filter(ImageFilter.BLUR)

    cropped = original.crop((x1, y1, x2, y2))

    for x in range(x1,x2):
       for y in range(y1,y2):
           pixels[x,y] = (x, y, 100)


    # Display both images
    original.show()
    blurred.show()
    cropped.save('C:/Users/natha/Desktop/car_plate2.jpg')

    # save the new image
    blurred.save("blurred.png")

except:
    print("Unable to load image")