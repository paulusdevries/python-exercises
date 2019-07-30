from cryptography.fernet import Fernet
from save_game import SaveGame
import getpass

passwfile = SaveGame('shadow')

with open('keyfile') as readfile:
    key = readfile.readline()
cipher_suite = Fernet(key)
password = getpass.getpass("Password to be stored: ")

cipher_text = cipher_suite.encrypt(password.encode())
passwfile.saveBytes(cipher_text)
