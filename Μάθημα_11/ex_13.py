from random import seed
from random import randrange
from datetime import datetime

# globals
kind = {"heart", "diamond", "spade", "club"}
number = {"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}
deck = {(k, n) for k in kind for n in number}


# functions
# Αυτή η συνάρτηση υπολογίζει το άθροισμα των αριθμών των καρτών στο χέρι
def hand_value(hand):
    total = 0
    ace = False
    for card in hand:
        n = card[1]
        if n == "Jack" or n == "Queen" or n == "King":
            total += 10
        elif n == "Ace":
            ace = True
            total += 1
        else:
            total += n

    if ace:
        if total + 10 <= 21:
            total += 10

    return total


def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        print(f"Your hand: {hand} \nYour number: {hand_value(hand)}")
        choice = input("Draw another card, 'yes' or 'no': ")
        if choice == "yes":
            hand.add(deck.pop())

            if hand_value(hand) >= 21:
                return hand_value(hand)
        elif choice == "no":
            return hand_value(hand)


def computer(value_player, hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        value = hand_value(hand)
        if value >= 21:
            return value
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())



def main():
    seed(datetime.now())  # once, before randint call

    rounds = 0
    score = [0, 0]

    while True:
        print("=" * 15)
        print("Round " + str(rounds) + ":")
        print("=" * 15)
        player_hand = set()
        player_value = player(player_hand)

        print(f"Your hand: {player_hand} \nTotal number: {player_value}")
        if player_value == 21:
            print("You won!")
            result = "player"
        elif player_value > 21:
            print("You lost!")
            result = "computer"
        else:
            print("Computer plays...")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)

            print(f"Computer's hand: {computer_hand} \nTotal number: {computer_value}")

            if computer_value > 21:
                print("Computer messed up. You won!")
                result = "player"
            else:
                print("Computer wins!")
                result = "computer"

            if result == "player":
                score[0] += 1
            else:
                score[1] += 1

            print(f"Score: Player - {score[0]} : {score[1]} - Computer")
            choice = input("Play again, 'yes' or 'no': ")

            if choice == "no":
                print("Thanks for playing! Bye bye!")
                quit()


main()


