from cryptography.fernet import Fernet
from save_game import SaveGame

save_key = SaveGame('keyfile')
save_key.saveBytes(Fernet.generate_key())
