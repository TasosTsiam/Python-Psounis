from random import seed
from random import randrange
from datetime import datetime


def player1_pick():
    while True:
        card1 = randrange(len(list_deck))
        if list_deck[card1] not in player1 and list_deck[card1] not in player2:
            player1.add(list_deck.pop(card1))
            return True


def player2_pick():
    while True:
        card2 = randrange(len(list_deck))
        if list_deck[card2] not in player1 and list_deck[card2] not in player2:
            player2.add(list_deck.pop(card2))
            return True


def play():
    print("Picking a card for a player!")
    while True:
        i = randrange(2)
        if i == 0:
            player1_pick()
        else:
            player2_pick()
        if len(list_deck) == 0:
            return player1, player2
            

seed(datetime.now())

kind = {"heart", "diamond", "spade", "club"}
number = {"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}
deck = {(k, n) for k in kind for n in number}

player1 = set()
player2 = set()
list_deck = list(deck)




p1, p2 = play()

if len(p1) > len(p2):
    print(f"Player 1 has won! \nPlayer 1 total cards: {len(p1)}\nPlayer 2 total cards: {len(p2)}")
elif len(p1) < len(p2):
    print(f"Player 2 has won! \nPlayer 1 total cards: {len(p1)}\nPlayer 2 total cards: {len(p2)}")
else:
    print(f"It's a Draw! \nPlayer 1 total cards: {len(p1)}\nPlayer 2 total cards: {len(p2)}")
