
class SaveGame:
    def __init__(self, filename = ""):
        if filename == "":
            self.filename = input("Enter the name for the file where you want to save your game: ")
        else:
            self.filename = filename



    def saveGame(self, game):
        with open(self.filename, 'a') as savegame:
            savegame.write(game)


    def saveBytes(self, bijtjes):
        with open(self.filename, 'wb') as savebijtjes:
            savebijtjes.write(bijtjes)
