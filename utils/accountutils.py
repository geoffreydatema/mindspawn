import base64

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
    # zeros = np.zeros((1024, 512, 3), dtype=np.uint8)
    raw_data = data
    
    while len(raw_data) > 0:
        print(raw_data[:8])
        #!* iterate through bits and write to pixels
        raw_data = raw_data[8:]

    # img = Image.fromarray(data)
    # img.save(path)