hidden_numbers = [100, 4, 2, 1, 3, 2, 4, 3]
revealed = ["x", "x", "x", "x", "x", "x", "x", "x"]
count = 0
best_score = 0
while "x" in revealed:
    count += 1
    card1 = int(input("Enter your first number between 0-7: \n"))
    number1 = hidden_numbers[card1]
    revealed[card1] = str(number1)
    print(revealed)

    card2 = int(input("Enter your second number between 0-7: \n"))
    number2 = hidden_numbers[card2]
    revealed[card2] = str(number2)
    print(revealed)

    if number1 == number2 and card1 != card2:
        if "x" in revealed:
            print("You found it. Keep going!")
        else:
            if best_score == 0:
                best_score = count
            if best_score > count:
                best_score = count
            print("You made it!")
            print("You made", count, "tries")
            print("Your best score is", best_score)
            answer = input("You wanna play again mate? Yes or No?: \n")

            if answer == "Yes":
                revealed = ["x", "x", "x", "x", "x", "x", "x", "x"]
                count = 0
                print("Restarted")
    else:
        revealed[card1] = "x"
        revealed[card2] = "x"
        print("Cards do not match. Hiding again :D")
        print(revealed)
