"""
# We can not only read/write txt, csv etc files but can also play with binary (images/gif/audio/video etc)
# We have library named "pillow" (install using: pip install pillow)
"""

# To run this file, since we are accepting file names in sys.argv, so run it as: python main.py cat1.png cat2.png

import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    images.append(Image.open(arg))

images[0].save(
    "cat.gif", save_all=True, append_images=[images[1]], duration=200, loop=0, disposal=2
)

# cat.gif: name of the saved file
# save_all = True is to save all the frames that we are going to pass to it
# append_images=[images[1]] is to append images[1] to images[0]
# duration = 200 is to show an image for those 200 milliseconds
# loop = 0 is to loop infinitely
# disposal = 2 is to clear previous frame before drawing next frame.
"""
So, we are doing: 
to images[0], append immages[1], and save it with name cat.gif and loop this infinitely by showing each image for 200 milliseconds
"""
