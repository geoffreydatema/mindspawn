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

def bitmapListTo2DArray(data, row_size):
    result = []
    row = []
    column_counter = 0
    for pixel in data:
        row.append(pixel)
        column_counter += 1
        if column_counter == row_size:
            result.append(row)
            column_counter = 0
            row = []
    return result

def jdump(data):
    return json.dumps(data)

def jparse(data):
    parsed_data = {}
    try:
        parsed_data = json.loads(data)
    except:
        print("could not read decrypted data")
    return parsed_data

def bencode(data):
    return "".join("{0:08b}".format(ord(x)) for x in data)

def bdecode(data):
    raw_data = data
    index = 0
    result = ""
    while len(raw_data) > 0:
        if len(raw_data) > 0:
            result += chr(int(raw_data[:8], 2))
            raw_data = raw_data[8:]
        else:
            break
    return result