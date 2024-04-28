import base64
import numpy as np
from PIL import Image

def minihash(data):
    if len(data) < 8:
        while len(data) < 8:
            data += "0"
    number = ""
    for c in data:
        number += str(ord(c))
    return str(int(number))

def stepcrypt(data, key):
    raw_data = data
    encrypted_data = ""
    while len(raw_data) > 0:
        for k in key:
            if len(raw_data) > 0:
                character = ord(raw_data[0])
                offset = int(k)
                offset_character = character - offset
                if offset_character < 0:
                    print("hit ASCII limit during stepcrypt!")
                    encrypted_data += "0"
                else:
                    encrypted_data += chr(offset_character)
                raw_data = raw_data[1:]
            else:
                break

    return base64.b64encode(encrypted_data.encode("utf-8"))

def destepcrypt(data, key):
    encrypted_data = base64.b64decode(data).decode("utf-8")
    decrypted_data = ""
    while len(encrypted_data) > 0:
        for k in key:
            if len(encrypted_data) > 0:
                character = ord(encrypted_data[0])
                offset = int(k)
                offset_character = character + offset
                if offset_character > 127:
                    print("hit ASCII limit during destepcrypt!")
                    decrypted_data += "0"
                else:
                    decrypted_data += chr(offset_character)
                encrypted_data = encrypted_data[1:]
            else:
                break

    return decrypted_data

def writeCyphermap(data, path):
    pixel_data = np.zeros((1024, 512, 3), dtype=np.uint8)
    raw_data = data
    print(raw_data)
    print(len(raw_data) // 8)

    row_count = 1024
    # image width / 8
    column_offset_count = 64
    while len(raw_data) > 0:
        for r in range(row_count):
            for o in range(column_offset_count):
                if len(raw_data) > 0:
                    for c in range(8):
                        if raw_data[c] == "1":
                            pixel_data[r, (o * 8) + c] = [255, 255, 255]
                    raw_data = raw_data[8:]
                else:
                    break
    
    img = Image.fromarray(pixel_data)
    img.save(path)