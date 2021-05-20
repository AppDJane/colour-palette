########################################################################################################################
#
#
# Author: AppDJane
#
# Date: May 6th, 2021
#
# Content:
# With the following program the user can provide a filepath to an image and he / she get as answer the top 10 most
# common colours in that image (saved as an image output file.
#
#
########################################################################################################################

import extcolors
from PIL import Image, ImageDraw


def save_output(colors, boxsize=20, spacebetween=5, outfile="top10colors.png"):
    num_colors = len(colors)

    # Creates a new image with the given mode and size.
    top10color_img = Image.new('RGB', ((boxsize+spacebetween) * num_colors, boxsize))

    # Creates an object that can be used to draw in the given image.
    draw = ImageDraw.Draw(top10color_img)

    posx = 0
    for color in colors:
        #
        draw.rectangle([posx, 0, posx + boxsize, boxsize], fill=color)
        posx = posx + boxsize + spacebetween

    del draw
    top10color_img.save(outfile, "PNG")

# ---------------------------------------------------------------------------------------------------------------------

filename = input("Image to upload: ")
outputfile = input("Image name: ")



colors, pixel_count = extcolors.extract_from_path(filename)

# print(colors)
color_array = []
for i in range(9, len(colors)):
    color_array.append((colors[i][0]))

print(color_array)

# aimed format: [(23, 8, 16), (200, 111, 43), (240, 174, 98), (44, 59, 50), (240, 203, 151), (151, 64, 32), (217, 167, 106), (247, 221, 184), (156, 152, 103), (146, 106, 56)]
# print(pixel_count)
save_output(color_array, outfile=outputfile)