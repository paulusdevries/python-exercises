from cows_n_bulls import CowsNBulls
from save_game import SaveGame

cowsnbulls = CowsNBulls()
save = SaveGame()
cowsnbulls.printCowsnbulls()
save.saveGame(f"\nYou've won in {str(cowsnbulls.loopGame())} rounds")
