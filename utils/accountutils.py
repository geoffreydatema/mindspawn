import math
import base64
import numpy as np
from utils.utils import *

def initAccountFile(username):
    account = {
        "username": username,
        "level": "1"
    }
    return account

def save(data, key, path):
    hashword = minihash(key)
    encrypted_data = stepcrypt(jdump(data), hashword)
    fwritebytes(encrypted_data, rf"{path}\{data["username"]}.txt")
    writeCyphermap(bencode(str(encrypted_data)[2:-1]), data["username"], r"C:\Working\mindspawn\data")

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

def writeCyphermap(data, username, path):
    pixel_data = np.zeros((1024, 512, 3), dtype=np.uint8)
    raw_data = data
    block_count = len(raw_data) // 8

    for x in range(9):
        row_col_size = 2 ** x
        if math.sqrt(block_count) > row_col_size:
            continue
        else:
            block_width = 512 // row_col_size
            block_height = block_width * 2
            cell_size = block_width // 2

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

    iwrite(pixel_data, rf"{path}\{username}.png")

def readCyphermap(path):
    raw_data = iread(path)

    # determine cell (and therefore block) size by reading pixels in rows until we get a pattern of black -> white or white -> black
    solved = False
    colours = []
    cell_pixel_count = 0
    index = 0

    while solved == False:
        current_pixel = raw_data[index][0]
        colours.append(current_pixel)

        if len(colours) > 0:
            if current_pixel != colours[index - 1]:
                solved = True
            else:
                cell_pixel_count += 1
        index += 1

    pixel_data = bitmapListTo2DArray(raw_data, 512)

    cell_size = cell_pixel_count
    row_col_size = (512 // cell_size) // 2  
    block_width = 512 // row_col_size
    block_height = block_width * 2
    binary_characters = ""

    # row_col_size rows of blocks in the cyphermap
    for rcy in range(row_col_size):
        # row_col_size columns of blocks in the cyphermap
        for rcx in range(row_col_size):
                # 4 rows of cells per block
                for by in range(4):
                    # 2 columns of cells per block
                    for bx in range(2):
                        if pixel_data[(rcy * block_height) + (by * cell_size)][(rcx * block_width) + (bx * cell_size)][0] == 0:
                            binary_characters += "0"
                        else:
                            binary_characters += "1"

    return binary_characters