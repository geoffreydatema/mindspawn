import json

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

def jparse(data):
    return json.loads(data)

def bencode(data):
    return "".join("{0:08b}".format(ord(x)) for x in data)
