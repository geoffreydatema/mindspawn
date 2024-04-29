import json
from PIL import Image

def fread(path):
    data = None
    with open(path, "r") as file:
        data = file.read()
    return data

def freadbytes(path):
    data = None
    with open(path, "rb") as file:
        data = file.read()
    return data

def fwrite(data, path):
    with open(path, "w") as file:
        file.write(data)

def fwritebytes(data, path):
    with open(path, "wb") as file:
        file.write(data)

def iread(path):
    image = Image.open(path)
    pixel_data = list(image.getdata())
    return pixel_data

def iwrite(data, path):
    image = Image.fromarray(data)
    image.save(path)

def jparse(data):
    return json.loads(data)

def bencode(data):
    return "".join("{0:08b}".format(ord(x)) for x in data)
