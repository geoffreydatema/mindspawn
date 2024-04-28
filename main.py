from utils.utils import *
import utils.accountutils as accountutils

def main():
    # password = "very long password"
    # hashword = accountutils.minihash(password)

    # data = fread(r"C:\Working\mindspawn\data\TestAccount.txt")

    # encrypted_data = accountutils.stepcrypt(data, hashword)
    # fwritebytes(encrypted_data, r"C:\Working\mindspawn\data\cyphertext.txt")
    # decrypted_data = accountutils.destepcrypt(freadbytes(r"C:\Working\mindspawn\data\cyphertext.txt"), hashword)

    # account = jparse(decrypted_data)
    # print(account)

    test_data = bencode("very special secret message to be encoded into binary very special secret message to be encoded into binary very special secret message to be encoded into binary very special secret message to be encoded into binary")
    accountutils.writeCyphermap(test_data, r"C:\Working\mindspawn\data\image.png")

if __name__ == '__main__':
    main()