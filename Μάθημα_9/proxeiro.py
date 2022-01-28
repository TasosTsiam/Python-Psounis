from random import seed
from random import randrange
from datetime import datetime
seed(datetime.now())

words = [
"on",
"slave",
"judge",
"facade",
"lodge",
"crevice",
"bird",
"goalkeeper",
"desert",
"hierarchy"
]

# initialization

hidden_word = words[randrange(len(words))]
guessed_letters = []
miss = 0

# welcome

print("Let's play kremala!")

print("_______")
print("|     |")
print("|")
print("|")
print("|")
print("|")
print("|")

# input check

while True:
    print("")
    letter = input("Enter a letter: ").lower().strip()

    if letter in guessed_letters:
        print("You have already entered that letter.")
    elif not letter.isalpha():
        print("Please enter a LETTER")
    elif len(letter) != 1:
        print("Please enter A letter")
    else:
        guessed_letters.append(letter)

        found = True
        for char in hidden_word:
            if char in guessed_letters:
                print(char + " " ,end="")
            else:
                print("_ " ,end="")
                found = False
        print("")

        if found:
            print("")
            print("Bravo! You're not a loser!")
            break

    # graphic

        if letter not in hidden_word:
            miss += 1
        if miss == 1:
            print("_______")
            print("|     |")
            print("|     O")
            print("|")
            print("|")
            print("|")
            print("|")
        elif miss == 2:
            print("_______")
            print("|     |")
            print("|     O")
            print("|     |")
            print("|")
            print("|")
            print("|")
        elif miss == 3:
            print("_______")
            print("|     |")
            print("|     O")
            print("|    /|")
            print("|")
            print("|")
            print("|")
        elif miss == 4:
            print("_______")
            print("|     |")
            print("|     O")
            print("|    /|\\")
            print("|")
            print("|")
            print("|")
        elif miss == 5:
            print("_______")
            print("|     |")
            print("|     O")
            print("|    /|\\")
            print("|    /")
            print("|")
            print("|")
        elif miss == 6:
            print("_______")
            print("|     |")
            print("|     O")
            print("|    /|\\")
            print("|    / \\")
            print("|")
            print("|")

            # break + message

        elif (miss > 6 and miss < 10):
            print("")
            print(f"You have {10-miss} misguesses left")
        elif miss == 10:
            print("You're a loser!")
            break
