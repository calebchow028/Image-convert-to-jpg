#import os and sys
import os, sys

#import Image method from pillow
from PIL import Image

#extra library for HEIC
import pillow_heif

#register HEIC/HEIF support with pillow
pillow_heif.register_heif_opener()

#loop through all image files
for input in sys.argv[1:]:
    #split the file name into the name and the extension
    name, ext = os.path.splitext(input)

    #set output as name + jpg
    output = name + ".jpg"

    #check if input is different than output
    if input != output:
        #try and except
        try:
            #set im as the opened image and close the image
            with Image.open(input) as im:
                im.save(output)

                #print message
                print(f"converted {input} > {output}")
        except OSError:
            #print cannot convert
            print(f"cannot convert {input}")