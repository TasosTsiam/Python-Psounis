from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

print("")
print("")


my_list = ["scissors", "paper", "rock"]
victory = 3
user_score = 0
computer_score = 0
round = 0
my_dict = {}

print("Lets play rock, paper, scissors!")
print("Whoever reaches 3 victories, wins the game!")
print("")
print("")
while user_score < victory and computer_score < victory:
    user_input = input("Pick your choice: ")
    print("")
    while user_input != my_list[0] and user_input != my_list[1] and user_input != my_list[2]:
        print("Invalid choice. You have to type either 'rock', or 'paper', or 'scissors'.")
        user_input = input("Pick your choice: ")
        print("")

    if user_input == my_list[0]:
        computer_choice = my_list[randrange(len(my_list))]
        if computer_choice == user_input:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "Its a draw!")
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
        elif computer_choice == my_list[1]:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "You won!")
            user_score += 1
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
        else:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "You lost!")
            computer_score +=1
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")

    if user_input == my_list[1]:
        computer_choice = my_list[randrange(len(my_list))]
        if computer_choice == user_input:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "Its a draw!")
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
        elif computer_choice == my_list[0]:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "You lost!")
            computer_score +=1
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
        else:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "You won!")
            user_score += 1
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")

    if user_input == my_list[2]:
        computer_choice = my_list[randrange(len(my_list))]
        if computer_choice == user_input:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "Its a draw!")
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
        elif computer_choice == my_list[0]:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "You won!")
            user_score += 1
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
        else:
            print("Your choice      : " + user_input + "\n" + "Computer's choice: " + computer_choice + "\n" + "You lost!")
            computer_score +=1
            print("Your score      : " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
            print("")
    round += 1

    #Εντελώς σωστός τρόπος επίλυσης, να αποθηκεύω τους γύρους κάθε φορά κάπου, αλλά αν και καθόλου κομψός,
    #καθώς με μια λίστα όπως έκανε ο Ψούνης, γίνεται κομψότατο, χαίρομαι γιατί χρησιμοποίησα και dictionary,
    #δείχνοντας στον εαυτό μου πως έμαθα σε καλό επίπεδο πως να τα χρησιμοποιώ, σ' αυτό το μάθημα!
    my_dict["round " + str(round)] = {"Player" : user_input}, {"Computer" : computer_choice}, {"Score" : str(user_score) + "-" + str(computer_score)}

    #Optional print to show the results of each round, analytically.
    print("Round " + str(round), my_dict["round " + str(round)])
if user_score == victory:
    print("You won the game!")
else:
    print("You lost the game!")

print("total rounds of the game : " + str(round))
print(my_dict)
