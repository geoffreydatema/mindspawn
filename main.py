from utils.utils import *
import utils.accountutils as accountutils
import base64

def main():

    account = accountutils.initAccountFile(username="oystertheory")

    password = "very long password"
    
    accountutils.save(account, password, r"C:\Working\mindspawn\data")

    #!* make load functions for both text and cyphermap

    # decrypted_data = accountutils.destepcrypt(freadbytes(r"C:\Working\mindspawn\data\oystertheory.txt"), hashword)
    # loadedAccount = jparse(decrypted_data)

    # data = accountutils.readCyphermap(r"C:\Working\mindspawn\data\test.png")
    # decoded_data = bdecode(data)
    # print(decoded_data)

if __name__ == '__main__':
    main()