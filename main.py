from utils.utils import *
import utils.accountutils as accountutils
import base64

def main():

    # account = accountutils.initAccountFile(username="oystertheory")

    password = "very long password"
    
    # accountutils.save(account, password, r"C:\Working\mindspawn\data")

    account = accountutils.loadSaveFile(r"C:\Working\mindspawn\data\oystertheory.txt", password)
    print(f"account read from save file: {account}")

    account2 = accountutils.loadCyphermap(r"C:\Working\mindspawn\data\oystertheory.png", password)
    print(f"account read from cyphermap: {account2}")

if __name__ == '__main__':
    main()