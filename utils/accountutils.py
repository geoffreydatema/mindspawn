import math
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

def writeCyphermapByRows(data, path):
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

def writeCyphermap(data, path):
    pixel_data = np.zeros((1024, 512, 3), dtype=np.uint8)
    raw_data = data

    print(raw_data)
    print("---------------")
    print(f"number of bytes: {len(raw_data) // 8}")

    block_count = len(raw_data) // 8
    print(f"block_count // 2: {block_count // 2}")

    print(f"first character of data string is {raw_data[0]} {type(raw_data[0])}")

    for x in range(9):
        row_col_size = 2 ** x
        if math.sqrt(block_count) > row_col_size:
            continue
        else:
            block_width = 512 // row_col_size
            block_height = block_width * 2
            cell_size = block_width // 2
            print("----------------------")
            print(f"blocks rows and columns: {row_col_size} x {row_col_size}")
            print(f"total number of blocks (bytes): {row_col_size * row_col_size}")
            print(f"cell size: {cell_size} x {cell_size}")

            # row_col_size rows of blocks in the cyphermap
            for rcy in range(row_col_size):
                # row_col_size columns of blocks in the cyphermap
                for rcx in range(row_col_size):
                        # 4 rows of cells per block
                        for by in range(4):
                            # 2 columns of cells per block
                            for bx in range(2):                                
                                if len(raw_data) > 0:
                                    if raw_data[0] == "1":
                                        # cell is cell_size tall                                       
                                        for cy in range(cell_size):
                                            # cell is cell_size wide
                                            for cx in range(cell_size):
                                                pixel_data[(rcy * block_height) + (by * cell_size) + cy, (rcx * block_width) + (bx * cell_size) + cx] = [255, 255, 255]
                                    raw_data = raw_data[1:]
                                else:
                                    break
            break
    
    img = Image.fromarray(pixel_data)
    img.save(path)