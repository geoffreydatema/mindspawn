import base64

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

def singleOffsetEncrypt(data, key):
    result = ""
    for c in data:
        result += chr(ord(c) + key)
    return result

def singleOffsetDecrypt(data, key):
    result = ""
    for c in data:
        result += chr(ord(c) - key)
    return result

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

def main():
    password = "very long password"
    hashword = minihash(password)

    data = fread(r"C:\Working\mindspawn\data\TestAccount.txt")

    encrypted_data = stepcrypt(data, hashword)
    fwritebytes(encrypted_data, r"C:\Working\mindspawn\data\cyphertext.txt")
    decrypted_data = destepcrypt(freadbytes(r"C:\Working\mindspawn\data\cyphertext.txt"), hashword)

    print(encrypted_data)
    print(decrypted_data)

    # !* parse the decrypted data as json

    

if __name__ == '__main__':
    main()