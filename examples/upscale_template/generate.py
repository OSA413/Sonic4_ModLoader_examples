#Let me know when Pillow learn how to export DDS

#https://pillow.readthedocs.io/en/stable/installation.html#notes
#https://pypi.org/project/Pillow/#files
#pip install Pillow (use pip3 for Linux)

import os
import subprocess
import glob
from PIL import Image, ImageFont, ImageDraw#, DdsImagePlugin

os.chdir(os.path.dirname(__file__))

PATH_TO_WAIFU2X = os.path.abspath("../../dependencies/waifu2x-ncnn-vulkan/waifu2x-ncnn-vulkan")

def convert_to_png(file_dds):
    with open("gimp-convert.bat", "r") as f:
        main_script = f.read()

    with open("gimp-convert-png.fu", "r") as f:
        script = f.read().replace("\n", " ").replace("{{filename}}", file_dds) \
            .replace("{{output}}", file_dds[:-3]+"PNG").replace("\\", "\\\\").replace("\"", "\\\"")

    subprocess.run(main_script + " \"" + script + "\" --batch \"(gimp-quit 1)\"",
        cwd = os.getcwd(),
        shell = True)

def convert_to_dds(file_png):
    with open("gimp-convert.bat", "r") as f:
        main_script = f.read()

    with open("gimp-convert-dds.fu", "r") as f:
        script = f.read().replace("\n", " ").replace("{{filename}}", file_png) \
            .replace("{{output}}", file_png[:-3]+"DDS").replace("\\", "\\\\").replace("\"", "\\\"")

    subprocess.run(main_script + " \"" + script + "\" --batch \"(gimp-quit 1)\"",
        cwd = os.getcwd(),
        shell = True)

def generate_and_save(file_png):
    subprocess.run(PATH_TO_WAIFU2X +
                    " -i \""+file_png+"\" -o \""+file_png+"\"" +
                    " -n 3 -s 2",
                   cwd = os.getcwd(),
                   shell = True)


the_files = glob.glob("./place root here/**/*.dds", recursive = True)

for i in range(len(the_files)):
    f = the_files[i]
    file = os.path.abspath(f.replace("\\", "/"))
    print(file)
    print(str(i) + "/" + str(len(the_files)))
    convert_to_png(file)
    generate_and_save(file[:-3]+"png")
    generate_and_save(file[:-3]+"png")
    convert_to_dds(file[:-3]+"png")
    os.remove(file[:-3]+"png")

    other_place = file.replace("place root here", "converted")
    if not os.path.exists(os.path.dirname(other_place)):
        os.makedirs(os.path.dirname(other_place))
    os.rename(file, other_place)

