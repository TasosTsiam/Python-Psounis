from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

kind = {"heart", "diamond", "spade", "club"}
number = {"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}
deck = {(k, n) for k in kind for n in number}

player1 = set()
player2 = set()

# Μετατροπή του των καρτών σε list,
# για να μπορούμε να κάνουμε τις παρακάτω ενέργειες.

list_deck = list(deck)
for i in range(5):
    card1 = randrange(len(list_deck))
    player1.add(list_deck.pop(card1))
    card2 = randrange(len(list_deck))
    player2.add(list_deck.pop(card2))

# Καρέ του άσσου.
# Ενέργειες για το αν βρίσκεται 4 φορές
# στα φύλλα των παιχτών ο άσσος.
count = 0
for card in player1:
    if card[1] == "Ace":
        count += 1
if count == 4:
    print("Player 1 has Kare!")

for card in player2:
    if card[1] == "Ace":
        count += 1
if count == 4:
    print("Player 2 has Kare!")

# Κέντα.
# Ενέργειες για να δούμε αν οι παίχτες έχουν κέντα.
# Μας νοιάζουν μόνο οι αριθμοί στην κάθε κάρτα απ' τις 5,
# του κάθε παίχτη. Άρα φτιάχνουμε μια λίστα, την οποία και
# θα ταξινομήσουμε σε αύξουσα σειρά, που θα εμπεριέχει μόνο
# τους αριθμούς της κάθε κάρτας. Αν η διαφορά μεταξύ τους είναι
# μόνο 1, και στα 5 φύλλα, τότε έχουμε κέντα.
numbers_of_p1 = []
for card in player1:
    if card[1] == "Ace":
        numbers_of_p1.append(1)
    elif card[1] == "Jack":
        numbers_of_p1.append(11)
    elif card[1] == "Queen":
        numbers_of_p1.append(12)
    elif card[1] == "King":
        numbers_of_p1.append(13)
    else:
        numbers_of_p1.append(card[1])
numbers_of_p1.sort()

numbers_of_p2 = []
for card in player2:
    if card[1] == "Ace":
        numbers_of_p2.append(1)
    elif card[1] == "Jack":
        numbers_of_p2.append(11)
    elif card[1] == "Queen":
        numbers_of_p2.append(12)
    elif card[1] == "King":
        numbers_of_p2.append(13)
    else:
        numbers_of_p2.append(card[1])
numbers_of_p2.sort()

# Έλεγχος διαφοράς μεταξύ των 5 φύλλων.
kenta_count = 1
for pos in range(4):
    if numbers_of_p1[pos] == numbers_of_p1[pos + 1] - 1:
        kenta_count += 1
if kenta_count == 5:
    print("Player 1 has kenta!")

kenta_count2 = 1
for pos in range(4):
    if numbers_of_p2[pos] == numbers_of_p2[pos + 1] - 1:
        kenta_count2 += 1
if kenta_count2 == 5:
    print("Player 1 has kenta!")

print(player1)
print(player2)
