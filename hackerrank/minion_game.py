def minion_game(string):
    # in this exercise the Y is not considered as a vowel
    vowels = "AEOUI"

    # make sure string is all upper case
    string = string.upper()

    # create the empty starting letters for either stuart and kevin
    firstvowel = ""
    firstconsonant = ""

    # get thru the string to determine either the first vowel or consonant
    for i in range(len(string)):
        if string[i] in vowels:
            do = "nothing"
            print(f"{string[i]} is the first vowel so do {do}.")
            firstvowel = string[i]
            break

    for i in range(len(string)):
        if string[i] not in vowels:
            firstconsonant = string[i]
            pos = i
            break

    # iterate thru the string starting with either the vowel or the consonant

    for consonant in string:
        print(consonant)



# your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)