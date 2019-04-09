#Let me know when Pillow learn how to export DDS

#https://pillow.readthedocs.io/en/stable/installation.html#notes
#https://pypi.org/project/Pillow/#files
#pip install Pillow (use pip3 for Linux)

import os
import subprocess
import glob
from PIL import Image, ImageFont, ImageDraw#, DdsImagePlugin

os.chdir(os.path.dirname(__file__))

PATH_TO_MOGRIFY = os.path.abspath("../../dependencies/ImageMagick/mogrify")

def convert_to_dds(file):
    """
    Pillow can't export DDS at this moment
    As for now I'll use ImageMagick to do this
    P.S. - some old versions generate broken DDS
    Tested versions:
        Windows: 7.0.8
    """
    subprocess.run(PATH_TO_MOGRIFY +
                    " -format dds -define dds:compression=dxt1 " +
                    "\""+file+"\"",
                   cwd = os.getcwd(),
                   shell = True)

def generate_and_save(file):
    word = os.path.basename(file)[:-4]+" "*30
    word = word[:30]
    words = []
    for i in range(len(word)//6):
        words.append(word[i*6 : (i+1)*6])

    word = "\n".join(words)

    img_size = int(54)
    fnt_size = int(8)

    img = Image.new("RGB", (img_size, img_size), color = "white")
    fnt = ImageFont.truetype("../../shared/fnt/PixelOperatorMono8-Bold.ttf", fnt_size)

    draw = ImageDraw.Draw(img)
    draw.text((3,1), word, font=fnt, fill="black")

    file = file.replace("place root here", "output")

    dr = os.path.dirname(file)
    if not os.path.exists(dr):
        os.makedirs(dr)

    file_png = file[:-3]+"png"

    img.save(file_png)
    return file, file_png




the_files = glob.glob("./place root here/**/*.dds", recursive = True)

for i in the_files:
    file = os.path.abspath(i.replace("\\", "/"))
    file, file_png = generate_and_save(file)
    convert_to_dds(file_png)
    os.remove(file_png)

    #dealing with case sensitivity
    if file[-1] == "S":
        #test this on linux
        os.rename(file[:-3]+"dds", file[:-3]+"DDS")
