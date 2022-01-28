while True:
    user_input_name = input("Enter your name: ")
    user_input_surname = input("Enter your surname: ")
    user_input_name = user_input_name.strip()
    user_input_surname = user_input_surname.strip()
    if user_input_name.isalpha() and user_input_surname.isalpha():
        message_to_user = f"Hello {user_input_name.title()} {user_input_surname.title()}!"
        v1 = "-"
        print("+" + v1.center(28, "-") + "+")
        print("|" + message_to_user.center(28) + "|")
        print("+" + v1.center(28, "-") + "+")
        break
    else:
        print("Please, type only characters. Or else Imma search for you.")
