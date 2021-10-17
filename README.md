# createImage.py
Python-based image generator with a web API
---
Documentation coming soon...

## Usage

- Clone this repository
```bash
git clone https://github.com/piciakk/createImage.py
```
- Open the cloned folder
```bash
cd createImage.py
```
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

*Documentation coming soon...*