import random

words = []
count = 0
while count < 10:
    count += 1
    words.append(input(f"Type #{count} nederlands zelfstandig naamwoord in:"))


def geussing():
    count = 0
    wordpos = 0
    limit = 10
    hangman = ""
    guessed = ""
    roundguess = ""
    word = words[random.randint(0,9)]
    while True:
        if limit < 1:
            print(f"Je kansen zijn op.")
            break
        if guessed == word:
            print(f"Het is {word}. Je hebt in {count} gewonnen")
            break
        hangman = input("Letter of woord: ")
        wordpos = 0
        if len(hangman) > 1:
            if hangman != word:
                print(f"Verkeerd geraden: het is {word}")
                print("Geen kansen meer")
                break
            else:
                print(f"Gewonnen in {count} rondes")
                break
        elif len(hangman) == 1:
            for char in list(word):
                roundguess = ""
                if hangman == char:
                    print(f"{hangman} komt voor op pos {wordpos}")
                    roundguess = roundguess + hangman
                else:
                    roundguess = roundguess + "."
                wordpos += 1
            print(roundguess)
        guessed = roundguess
        count += 1
        limit -= 1


geussing()
