from PIL import Image, ImageDraw, ImageFont
import os
import time
import threading

def makeImage(photoWidth, photoHeight, Background, Text):
    # make background
    img = Image.new('RGB', (photoWidth, photoHeight), color = (Background["color"][0], Background["color"][1], Background["color"][2]))
    # select font
    fnt = ImageFont.truetype('/usr/share/fonts/opentype/urw-base35/C059-BdIta.otf', Text["fontSize"])
    # add the text
    d = ImageDraw.Draw(img)
    d.text((Text["textPosition"][0], Text["textPosition"][1]), Text["text"], font=fnt, fill=(Text["color"][0], Text["color"][1], Text["color"][2]))
    # save
    img.save('static/currentImage.png')

def deleteImage():
    # wait
    time.sleep(0.1)
    # remove
    os.remove("static/currentImage.png")

def makeImageAndDeleteIt(photoWidth, photoHeight, Background, Text):
    # make image
    makeImage(photoWidth, photoHeight, Background, Text)
    # delete it
    threading.Thread(target=deleteImage).start()
