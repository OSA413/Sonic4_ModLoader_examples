#Let me know when Pillow learn how to export DDS
#https://pillow.readthedocs.io/en/stable/installation.html#notes
#https://pypi.org/project/Pillow/#files
import os
from PIL import Image, ImageFont, ImageDraw#, DdsImagePlugin

os.chdir(os.path.dirname(__file__))

word = "123456\n"*5
img_size = int(53)
fnt_size = int(8)

img = Image.new("RGB", (img_size, img_size), color = "white")
fnt = ImageFont.truetype("../../shared/fnt/PixelOperatorMono8-Bold.ttf", fnt_size)

draw = ImageDraw.Draw(img)
draw.text((2,1), word, font=fnt, fill="black")

img.save("test.png")

