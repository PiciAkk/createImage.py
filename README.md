# createImage.py
Python-based image generator with a web API
---

## Installation

- Clone this repository
```bash
git clone https://github.com/piciakk/createImage.py
```
- Open the cloned folder
```bash
cd createImage.py
```
- Install all the dependencies
```bash
pip install -r requirements.txt
```

## Usage

- Run the webserver
```bash
python main.py
```
- Send an API call, and download the output image (curl, and wget example)

```bash
curl --location --request POST 'localhost:5000' \
--form 'text="Hello World!"' \
--form 'fontSize="200"' \
--form 'textR="255"' \
--form 'textG="255"' \
--form 'textB="0"' \
--form 'textPositionX="10"' \
--form 'textPositionY="10"' \
--form 'bgR="73"' \
--form 'bgG="109"' \
--form 'bgB="137"' \
--form 'photoWidth="1920"' \
--form 'photoHeight="1080"' && \
wget localhost:5000/static/currentImage.png
```

This will generate an image with "Hello World" text, and save it in a file called "currentImage.png".

## Using as library

First: make a dictionary that will contain the properties of the text

```python
Text = {
  "text": "Hello World", # text
  "fontSize": 200, # font size
  "color": [255, 255, 0], # color R, G, and B of text
  "textPosition": [10, 10] # x position of text, and y position of text
}
```

Next: make a dictionary that will contain the properties of the background

```python
Background = {
  "color": [73, 109, 137] # color R, G, and B of background
}
```

Then make a variable for photoWidth, and photoHeight

```python
photoWidth = 1920

photoHeight = 1080
```

Then import the module, and generate the image with the recently created variables

```python
import imageMaker # import the module

imageMaker.makeImage(photoWidth, photoHeight, Background, Text)
# we pass the variables to the function
```

Congratulations, you created an image, and saved it to `static/currentImage.png`
