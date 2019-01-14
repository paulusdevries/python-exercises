# python exercise cows n bulls
import random

class CowsNBulls:

    def __init__(self):
        random.seed(a=random.randint(0, 10000))
        self.cownsbulls = [random.randint(0,9) for num in range(4)]
        self.userinput = []
        self.cows = 0
        self.bulls = 0
        self.rounds = 0
        print(f"--- Mastermind guessing game ---")


    def printCowsnbulls(self):
        print(self.cownsbulls)


    def singleRoundCowsnBulls(self):
        index = 0
        self.cows = 0
        self.bulls = 0
        for digit in self.userinput:
            # print(f"Computer: {self.cownsbulls[index]} User: {digit} Index: {index}")
            if digit == self.cownsbulls[index]:
                self.cows += 1
            elif digit in self.cownsbulls:
                self.bulls += 1
            index += 1

        return self.bulls, self.cows


    def loopGame(self):
        while self.userinput != self.cownsbulls:
            self.userinput = [int(num) for num in list(input('Enter a 4 digit number: '))]
            self.bulls, self.cows = self.singleRoundCowsnBulls()
            print(f"You have {self.cows} cows and {self.bulls} bulls")
            if self.cows == 4:
                print(f"Yippie you've won")
            self.rounds += 1
        return self.rounds


if __name__ == "__main__":
    game = CowsNBulls()
    game.printCowsnbulls()
    game.loopGame()
