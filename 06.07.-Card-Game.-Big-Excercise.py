print("          Pair the numbers!   ")
print("(your input should be between 1 and 8).")
print("")
print("Behind each 'x' there is a number that has an identical pair. Open two x's at a time until you pair them all.")
print("")
print("['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']")
print("")


core_list = [1, 4, 2, 3, 1, 3, 4, 2]
cnt = 0
best_score = 0
x_list = ["x", "x", "x", "x", "x", "x", "x", "x"]
original_x_list = ["x", "x", "x", "x", "x", "x", "x", "x"]


while True:
    while "x" in x_list:
        first_number = int(input("Type a number to open the equivelant position of x: "))
        if first_number > 8 or first_number < 1:
            print("You illiterate crap! Try again, only this time indeed between 1 and 8 :)")
            print("")
            continue

        string_first_number = str(core_list[first_number - 1])
        x_list[first_number - 1] = core_list[first_number - 1]
        print(x_list)
        print("")


        second_number = int(input("Type a second number to open the equivelant position of x:  "))
        if second_number > 8 or second_number < 1:
            print("You illiterate crap! Try again, only this time indeed between 1 and 8 :)")
            x_list[first_number - 1] = "x"
            print("")
            continue

        string_second_number = str(core_list[second_number - 1])
        x_list[second_number - 1] = core_list[second_number - 1]
        print(x_list)
        print("")
        cnt += 1

        if string_first_number != string_second_number:
            x_list[second_number - 1] = "x"
            x_list[first_number - 1] = "x"
            print(x_list)
    else:
        print("Congratulations, you won!")
        print("")
        print("You succeeded after ", cnt, " times in total!")
        print("")
        if best_score == 0:
            best_score = cnt
        else:
            if cnt < best_score:
                best_score = cnt
        print("Your best score is: ", best_score)
        x_list = original_x_list[:]
        cnt = 0

    question = input("Do you want to play again? Type 'yes' or 'no': ")
    print("")
    if question == "no":
        quit()
    elif question == "yes":
        continue
    else:
        print("Type 'yes' or 'no' you semi retard, what you can't get?")
        question = input("Do you want to play again? Type 'yes' or 'no': ")
        while question == "yes":
            break
        else:
            if question == "no":
                quit()
            else:
                print("Okay you're a complete retard, get outa here!")
                quit()
