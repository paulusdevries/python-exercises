import random, os, sys

words = []
count = 0


def manual_list():
    global count
    global words
    while count < 10:
        count += 1
        words.append(input(f"Type #{count} nederlands zelfstandig naamwoord in:"))


def list_fromfile():
    global words
    with open('files/hangman.txt') as wordfile:
        words = wordfile.readlines()
        words

def drawHangman(number):
    if number == 0:
        print("  ________")
    elif number == 1:
        print("  ________")
    elif number == 2:
        print("      ____    \n"
              "  ___|    |____")
    elif number == 3:
        print("        |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 4:
        print("    ____\n"
              "   |    |\n"
              "        |\n"
              "        |\n"
              "        |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 5:
        print("    ____\n"
              "   |    |\n"
              "   0    |\n"
              "        |\n"
              "        |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 6:
        print("    ____\n"
              "   |    |\n"
              "   0    |\n"
              "   O\   |\n"
              "        |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 7:
        print("    ____\n"
              "   |    |\n"
              "   0    |\n"
              "  /O\   |\n"
              "        |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 8:
        print("    ____\n"
              "   |    |\n"
              "   0    |\n"
              "  /O\   |\n"
              "  /     |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 9:
        print("    ____\n"
              "   |    |\n"
              "   0    |\n"
              "  /O\   |\n"
              "  / \   |\n"
              "      __|_ \n"
              "  ___|    |____")
    elif number == 10:
        print("    ____\n"
              "   |    |\n"
              "  \\0/   |\n"
              "   O    |\n"
              "  / \   |\n"
              "      __|_ \n"
              "  ___|    |____")



def geussing():
    count = 0
    wordpos = 0
    limit = 10
    hangman = ""
    guessed = ""
    guessed_pos = {}
    roundguess = ""
    word = str(words[random.randint(0,9)]).rstrip('\n')
    while True:
        if limit < 1:
            print(f"Je kansen zijn op.")
            break
        hangman = input("Letter of woord: ")
        roundguess = ""
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
                if hangman == char:
                    print(f"{hangman} komt voor op pos {wordpos}")
                    guessed_pos.update({wordpos: hangman})
                wordpos += 1
        wordpos = 0
        for i in list(word):
            if wordpos in guessed_pos.keys():
                roundguess += i
            else:
                roundguess += "."
            wordpos += 1
        os.system('cls')
        guessed = roundguess
        if guessed == word:
            print(f"Het is {word}. Je hebt binnen {count} rondes gewonnen")
            break
        print(roundguess)
        count += 1
        drawHangman(count)
        limit -= 1


def usage():
    print(f"Gebruik: \n{sys.argv[0]} -h voor handmatig invoeren\n"
          f"{sys.argv[0]} -l voor lijst uit bestand files\\hangman.txt ")


if len(sys.argv) < 2:
    usage()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        manual_list()
        geussing()
    elif sys.argv[1] == "-l":
        list_fromfile()
        geussing()
    else:
        usage()
else:
    usage()
