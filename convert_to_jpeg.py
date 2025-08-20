#import os and sys
import os, sys

#import Image method from pillow
from PIL import Image

#extra library for HEIC
import pillow_heif

#register HEIC/HEIF support with pillow
pillow_heif.register_heif_opener()

#the folder that has images wanting to convert (change "." to the actual path)
input_folder = "."

#go through every file in the image folder
for filename in os.listdir(input_folder):
    #set input as the path to the file
    input = os.path.join(input_folder, filename)

    #separate the extension from input
    f, e = os.path.splitext(input)

    #set output's extension as .jpg
    output = f + ".jpg"

    #skip through all .jpg
    if e.lower() == ".jpg":
        continue

    #try and except OSError
    try:
        #set im as the opened image and close it afterwards
        with Image.open(input) as im:
            im.save(output)

            #print message
            print(f"Convert {input} > {output}")

    except OSError:
        #print message
        print(f"Cannot convert {input}")