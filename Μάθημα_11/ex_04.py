def input_float():
    user_input = input("Type a float: ").strip()
    v1 = True
    count = 0
    if user_input.isdigit():
        user_input = float(user_input)
        print(user_input)
    elif "." in user_input:
        for i in user_input:
            if i == ".":
                count += 1
        if count == 1:
            parts = user_input.partition(".")
            if parts[0].isdigit() and parts[2].isdigit():
                v1 = True
            else:
                v1 = False
        if v1 == True and count == 1:
            user_input = float(user_input)
            print(user_input)
        else:
            print("Invalid input.")
            input_float()
    else:
        print("Invalid input.")
        input_float()


input_float()
