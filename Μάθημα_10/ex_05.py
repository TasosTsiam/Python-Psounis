from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

words_list = ["tactical", "greasy", "delicious", "transformer", "qualifier",
"singularity", "despite", "nevertheless", "fortnite", "shotgun", "rifle", "launchpad",
"messi", "neymar", "ronaldo"]

hidden_word = words_list[randrange(len(words_list))]

guessed_letters = []

hidden_word_list = []

set1 = set(hidden_word)
set2 = set()

hidden_word_2 = hidden_word.upper()

count = 0

max_rounds = 10

round = 0

while True:
    round += 1
    print("")
    print(f"Round {round} / {max_rounds}.")
    user_input = input("Enter a letter: ")

    if user_input.lower() in guessed_letters:
        print("You 've already guessed this, try something else.")
        round -= 1
        continue
    if user_input.isalpha():
        if len(user_input) == 1:
            if hidden_word.find(user_input) != -1:
                print("")
                guessed_letters.append(user_input)
                for i in hidden_word:
                    if i == user_input.lower():
                        count += 1
                        underscore = i
                        hidden_word_list.append(i)
                        set2.add(i)

                    elif i in guessed_letters:
                        underscore = i
                        hidden_word_list.append(i)

                    else:
                        underscore = "_"
                    print(f"{underscore} ", end="")
            elif hidden_word_2.find(user_input) != -1:
                print("")
                guessed_letters.append(user_input.lower())
                for i in hidden_word:
                    if i == user_input.lower():
                        count += 1
                        underscore = i
                        hidden_word_list.append(i)
                        set2.add(i)

                    elif i in guessed_letters:
                        underscore = i
                        hidden_word_list.append(i)

                    else:
                        underscore = "_"
                    print(f"{underscore} ", end="")
            else:
                for i in hidden_word:
                    if i == user_input.lower():
                        count += 1
                        underscore = i
                        hidden_word_list.append(i)
                        set2.add(i)

                    elif i in guessed_letters:
                        underscore = i
                        hidden_word_list.append(i)

                    else:
                        underscore = "_"
                    print(f"{underscore} ", end="")

            print("")
            print("")
            print(f"the letter '{user_input}' is included {count} time(s) inside the word.")
            print("")
            count = 0
        else:
            round -= 1
            print(count)
            print("Invalid input. 1 letter at a time, please.")
    else:
        round -= 1
        print(count)
        print("Invalid input. Only letters please.")

    if set2.issuperset(set1):
        print("You won!")
        quit()
    if round == max_rounds and set2 != set1:
        print("You lost.")
        quit()
