from cryptography.fernet import Fernet

class GetPassword:
    def __init__(self):

        with open('keyfile') as readfile:
            key = readfile.readline()
        cipher_suite = Fernet(key)

        with open('shadow') as passwordfijl:
            cipher_text_file = passwordfijl.readline().encode()

        self.password = cipher_suite.decrypt(cipher_text_file)

    def retrievePassword(self):
        return self.password




