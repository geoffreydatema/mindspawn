from utils.utils import *
import utils.accountutils as accountutils

def main():
    password = "very long password"
    hashword = accountutils.minihash(password)

    data = fread(r"C:\Working\mindspawn\data\TestAccount.txt")

    encrypted_data = accountutils.stepcrypt(data, hashword)
    fwritebytes(encrypted_data, r"C:\Working\mindspawn\data\cyphertext.txt")
    decrypted_data = accountutils.destepcrypt(freadbytes(r"C:\Working\mindspawn\data\cyphertext.txt"), hashword)

    account = jparse(decrypted_data)
    print(account)

if __name__ == '__main__':
    main()