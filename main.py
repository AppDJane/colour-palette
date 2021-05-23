########################################################################################################################
#
#
# Author: AppDJane
#
# Date: May 23rd, 2021
#
# Content:
# With the following program the user can provide a filepath to an image. The top 10 colors will be displayed in a GUI.
#
#
########################################################################################################################

# ----------------------------------------------------- LIBRARIES ------------------------------------------------------
from tkinter import *
from math import *
from PIL import Image, ImageTk

# ----------------------------------------------------- FUNCTIONS ------------------------------------------------------


def get_key(e):
    return e[0]

def calculate_delta(color1, color2, delta):
    d = sqrt((color1[0]-color2[0])**2+(color1[1]-color2[1])**2+(color1[2]-color2[2])**2)
    return d < delta

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

# ---------------------------------------------- SELECT FILE TO ANALYSE ------------------------------------------------

file_path_nok = True

while file_path_nok:
    try:
        image_file = input("File to upload: ")
        img = Image.open(image_file)
        file_path_nok = False
    except:
        print("Not a valid file path. Please type filepath again.")

# ---------------------------------- TOP 10 COLORS CALCULATION CONSIDERING DELTA ---------------------------------------

# Returns an unsorted list of (count, pixel) values (list of colors) used in this image
colors = img.getcolors(img.size[0]*img.size[1])
colors.sort(reverse=True, key=get_key)
print(colors[:20])

top10 = {
    colors[0][1]: colors[0][0]
}
for c in colors:
    to_insert = True
    for k, v in top10.items():
        if calculate_delta(c[1], k, 24):
            to_insert = False
            break
    if to_insert:
        top10[c[1]] = c[0]
    if len(top10) >= 10:
        break
print(top10)

total_counts = 0
for x, y in top10.items():
    total_counts += y
print(total_counts)

# -------------------------------------------- GUI SETUP ---------------------------------------------------------------

window = Tk()
window.title("Top 10 colors")
window.config(padx=100, pady=50, bg="white")

# bg: background, fg: foreground
title_label = Label(text="Top 10 colors", fg='black', bg='white', font=('Arial', 50, 'bold'))
title_label.grid(column=2, row=0)
space_label = Label(text="     ", fg='black', bg='white', font=('Arial', 50))
space_label.grid(column=3, row=1)

color_label = Label(text="Color", fg='black', bg='white', font=('Arial', 14, 'bold'))
color_label.grid(column=1, row=2)
hex_label= Label(text="Color Code", fg='black', bg='white', font=('Arial', 14, 'bold'))
hex_label.grid(column=2, row=2)
pct_label= Label(text="Percentage", fg='black', bg='white', font=('Arial', 14, 'bold'))
pct_label.grid(column=4, row=2)

images = []
hex_labels = []
pct_labels = []
i = 0
for x, y in top10.items():
    print(x[:3])
    hex_labels.append(Label(window, text=f"#{rgb_to_hex(x[:3])}", fg='black', bg='white', justify=LEFT, font=('Arial', 12)).grid(column=2, row=i + 3))
    pct = y / total_counts
    pct_labels.append(
        Label(window, text=f"{round(pct,2)}", fg='black', bg='white', justify=LEFT, font=('Arial', 12)).grid(column=4,
                                                                                                         row=i + 3))
    image = Image.new('RGB', (200, 50), x)
    images.append(ImageTk.PhotoImage(image=image))
    c = Canvas(width=200, height=50, bg='white', highlightthickness=0)
    c.create_image(100, 25, image=images[i])
    c.grid(column=1, row=i+3)
    i += 1

window.mainloop()




