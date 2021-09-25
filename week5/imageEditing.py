#!/usr/bin/python3

# pip install pillow, if the PIL package ins't already installed
from PIL import Image

# Load an image
img = Image.open('missoula-college_logo.png')

# Get basic image info
print(img.format)
print(img.mode)
print(img.size)

# show the image
img.show()

# remove any transparency
(x_size, y_size) = img.size
for x in range(x_size):
    for y in range(y_size):
        (r, g, b, a) = img.getpixel((x, y))
        img.putpixel((x, y), (255 - r, 255 - g, 255 - b, a))

img.save('mytest.png')
