import requests
import os

x = requests.post("http://localhost:5000", data =
{
    'text': 'Hello World!',
    'fontSize': '200',
    'textR': '255',
    'textG': '255',
    'textB': '0',
    'textPositionX': '10',
    'textPositionY': '10',
    'bgR': '73',
    'bgG': '109',
    'bgB': '137',
    'photoWidth': '1920',
    'photoHeight': '1080'
})
if x.text == "Image generated...":
    img_data = requests.get("http://localhost:5000/static/currentImage.png").content
    with open('downloadedImage.png', 'wb') as handler:
        handler.write(img_data)
    os.system("tiv downloadedImage.png")
else:
    exit
