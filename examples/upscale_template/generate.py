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
PATH_TO_WAIFU2X = os.path.abspath("../../dependencies/waifu2x-ncnn-vulkan/waifu2x-ncnn-vulkan")

def convert_to_png(file_dds):
    subprocess.run(PATH_TO_MOGRIFY +
                    " -format png " +
                    "\""+file_dds+"\"",
                   cwd = os.getcwd(),
                   shell = True)

def convert_to_dds(file_png):
    """
    Pillow can't export DDS at this moment
    As for now I'll use ImageMagick to do this
    P.S. - some old versions generate broken DDS
    Tested versions:
        Windows: 7.0.8
    """
    subprocess.run(PATH_TO_MOGRIFY +
                    " -format dds -define dds:compression=dxt5 " +
                    "\""+file_png+"\"",
                   cwd = os.getcwd(),
                   shell = True)

def generate_and_save(file_png):
    subprocess.run(PATH_TO_WAIFU2X +
                    " -i \""+file_png+"\" -o \""+file_png+"\"" +
                    " -n 3 -s 2",
                   cwd = os.getcwd(),
                   shell = True)


the_files = glob.glob("./place root here/**/*.dds", recursive = True)
print("asd")
for i in the_files:
    file = os.path.abspath(i.replace("\\", "/"))
    print(file)
    convert_to_png(file)
    generate_and_save(file[:-3]+"png")
    generate_and_save(file[:-3]+"png")
    convert_to_dds(file[:-3]+"png")
    os.remove(file[:-3]+"png")

    #dealing with case sensitivity
    if file[-1] == "S":
        #test this on linux
        os.rename(file[:-3]+"dds", file[:-3]+"DDS")
