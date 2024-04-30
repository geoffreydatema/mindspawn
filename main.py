from utils.utils import *
import utils.accountutils as accountutils
import base64

def main():

    account = accountutils.initAccountFile(username="oystertheory")

    password = "very long password"
    
    # accountutils.save(account, password, r"C:\Working\mindspawn\data")

    # account = accountutils.loadSaveFile(r"C:\Working\mindspawn\data\oystertheory.txt", "very long password")
    # print(f"account read from save file: {account}")

    # account2 = accountutils.loadCyphermap(r"C:\Working\mindspawn\data\oystertheory.png", "very long password")
    # print(f"account read from cyphermap: {account2}")



    # accountutils.writeCyphermap(bencode(jdump(account)), "unencrypted_data", r"C:\Working\mindspawn\data")

    print(jparse(bdecode(accountutils.readCyphermap(r"C:\Working\mindspawn\data\unencrypted_data.png"))))

    #!* write save/loads for unencrypted cyphermaps

if __name__ == '__main__':
    main()