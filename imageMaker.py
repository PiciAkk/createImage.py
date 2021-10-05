from PIL import Image, ImageDraw, ImageFont

def makeImage(photoWidth, photoHeight, Background, Text):
    img = Image.new('RGB', (photoWidth, photoHeight), color = (Background["color"][0], Background["color"][1], Background["color"][2]))

    fnt = ImageFont.truetype('/usr/share/fonts/opentype/urw-base35/C059-BdIta.otf', Text["fontSize"])

    d = ImageDraw.Draw(img)
    d.text((Text["textPosition"][0], Text["textPosition"][1]), Text["text"], font=fnt, fill=(Text["color"][0], Text["color"][1], Text["color"][2]))

    img.save('static/currentImage.png')
