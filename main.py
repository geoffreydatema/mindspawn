from utils.utils import *
import utils.accountutils as accountutils
import base64

def main():

    account = accountutils.initAccountFile(username="oystertheory")

    # password = "very long password"
    
    # accountutils.save(account, password, r"C:\Working\mindspawn\data")

    # account = accountutils.loadSaveFile(r"C:\Working\mindspawn\data\oystertheory.txt", "very long password")
    # print(f"account read from save file: {account}")

    # account2 = accountutils.loadCyphermap(r"C:\Working\mindspawn\data\oystertheory.png", "very long password")
    # print(f"account read from cyphermap: {account2}")

    # test_pw = "test123"
    # test_hw = accountutils.minihash(test_pw)

    print(jdump(account))
    
    encrypted_data = accountutils.stepcrypt(jdump(account), accountutils.minihash("goodpassword"))

    decrypted_data = accountutils.destepcrypt(encrypted_data, accountutils.minihash("oodpassword"))
    print(decrypted_data)

if __name__ == '__main__':
    main()