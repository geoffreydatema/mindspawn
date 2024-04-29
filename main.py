from utils.utils import *
import utils.accountutils as accountutils
import base64

def main():

    # account = accountutils.initAccountFile(username="oystertheory")
    # print(str(account))
    # password = "very long password"
    # hashword = accountutils.minihash(password)
    # encrypted_data = accountutils.stepcrypt(str(account), hashword)
    # print(encrypted_data)
    # fwritebytes(encrypted_data, r"C:\Working\mindspawn\data\oystertheory.txt")
    # decrypted_data = accountutils.destepcrypt(freadbytes(r"C:\Working\mindspawn\data\oystertheory.txt"), hashword)
    # print(f"decrypted_data {decrypted_data}")
    # loadedAccount = jparse(decrypted_data)
    # print(loadedAccount)

    test_data = bencode("very special secret message")
    accountutils.writeCyphermap(test_data, "test", r"C:\Working\mindspawn\data")

    data = accountutils.readCyphermap(r"C:\Working\mindspawn\data\test.png")
    decoded_data = bdecode(data)
    print(decoded_data)

if __name__ == '__main__':
    main()