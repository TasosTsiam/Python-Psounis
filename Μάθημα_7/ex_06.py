#Ορίζουμε μια διδιάστατη λίστα.
triliza = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
#Σχηματίζουμε την τρίλιζα, με κάθε στοιχείο της κάθε λίστας που εμπεριέχεται
#στην διδιάστατη λίστα, στο αντίστοιχο σημείο του.
print("+---+---+---+")
print("| " + triliza[0][0] + " | " + triliza[0][1] + " | " + triliza[0][2] + " |")
print("+---+---+---+")
print("| " + triliza[1][0] + " | " + triliza[1][1] + " | " + triliza[1][2] + " |")
print("+---+---+---+")
print("| " + triliza[2][0] + " | " + triliza[2][1] + " | " + triliza[2][2] + " |")
print("+---+---+---+")

#Πρέπει να κατασκευάσουμε τον μηχανισμό για την επιλογή του επόμενου παίκτη,
#καθώς και τον μηχανισμό και την εκτύπωση αν έχουμε ισοπαλία(έχουμε φτάσει στον 9ο γύρο).

count = 0
while count < 9:
    player_O = int(input("Player 'O' plays! Check a Box: "))
    count += 1

    if player_O == 1:
        row = 0
        column = 0
    if player_O == 2:
        row = 0
        column = 1
    if player_O == 3:
        row = 0
        column = 2
    if player_O == 4:
        row = 1
        column = 0
    if player_O == 5:
        row = 1
        column = 1
    if player_O == 6:
        row = 1
        column = 2
    if player_O == 7:
        row = 2
        column = 0
    if player_O == 8:
        row = 2
        column = 1
    if player_O == 9:
        row = 2
        column = 2

    if triliza[row][column] == " ":
        triliza[row][column] = "O"

        print("+---+---+---+")
        print("| " + triliza[0][0] + " | " + triliza[0][1] + " | " + triliza[0][2] + " |")
        print("+---+---+---+")
        print("| " + triliza[1][0] + " | " + triliza[1][1] + " | " + triliza[1][2] + " |")
        print("+---+---+---+")
        print("| " + triliza[2][0] + " | " + triliza[2][1] + " | " + triliza[2][2] + " |")
        print("+---+---+---+")

        if triliza[0][0] == "O" and triliza[0][1] == "O" and triliza[0][2] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[1][0] == "O" and triliza[1][1] == "O" and triliza[1][2] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[2][0] == "O" and triliza[2][1] == "O" and triliza[2][2] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[0][0] == "O" and triliza[1][0] == "O" and triliza[2][0] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[0][1] == "O" and triliza[1][1] == "O" and triliza[2][1] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[0][2] == "O" and triliza[1][2] == "O" and triliza[2][2] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[0][0] == "O" and triliza[1][1] == "O" and triliza[2][2] == "O":
            print("Player 'O' has won!")
            quit()
        if triliza[0][2] == "O" and triliza[1][1] == "O" and triliza[2][0] == "O":
            print("Player 'O' has won!")
            quit()

    elif triliza[row][column] != " ":
        print("This box is filled. Try an empty one.")
        count -= 1
        continue

    if count == 9:
        break
    while True:
        player_X = int(input("Player 'X' plays! Check a Box: "))
        count += 1

        if player_X == 1:
            row = 0
            column = 0
        if player_X == 2:
            row = 0
            column = 1
        if player_X == 3:
            row = 0
            column = 2
        if player_X == 4:
            row = 1
            column = 0
        if player_X == 5:
            row = 1
            column = 1
        if player_X == 6:
            row = 1
            column = 2
        if player_X == 7:
            row = 2
            column = 0
        if player_X == 8:
            row = 2
            column = 1
        if player_X == 9:
            row = 2
            column = 2

        if triliza[row][column] == " ":
            triliza[row][column] = "X"

            print("+---+---+---+")
            print("| " + triliza[0][0] + " | " + triliza[0][1] + " | " + triliza[0][2] + " |")
            print("+---+---+---+")
            print("| " + triliza[1][0] + " | " + triliza[1][1] + " | " + triliza[1][2] + " |")
            print("+---+---+---+")
            print("| " + triliza[2][0] + " | " + triliza[2][1] + " | " + triliza[2][2] + " |")
            print("+---+---+---+")

            if triliza[0][0] == "X" and triliza[0][1] == "X" and triliza[0][2] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[1][0] == "X" and triliza[1][1] == "X" and triliza[1][2] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[2][0] == "X" and triliza[2][1] == "X" and triliza[2][2] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[0][0] == "X" and triliza[1][0] == "X" and triliza[2][0] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[0][1] == "X" and triliza[1][1] == "X" and triliza[2][1] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[0][2] == "X" and triliza[1][2] == "X" and triliza[2][2] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[0][0] == "X" and triliza[1][1] == "X" and triliza[2][2] == "X":
                print("Player 'X' has won!")
                quit()
            if triliza[0][2] == "X" and triliza[1][1] == "X" and triliza[2][0] == "X":
                print("Player 'X' has won!")
                quit()
            break

        elif triliza[row][column] != " ":
            print("This box is filled. Try an empty one.")
            count -= 1
            continue

print("It's a draw!")
