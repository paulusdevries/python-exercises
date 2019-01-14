
class SaveGame:
    def __init__(self):
        self.filename = input("Enter the name for the file where you want to save your game: ")


    def saveGame(self, game):
        with open(self.filename, 'a') as savegame:
            savegame.write(game)
