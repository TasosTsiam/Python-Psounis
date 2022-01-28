def print_name(first_name, surname, details=False, second_name="", second_surname=""):
    if details:
        if second_name != "":
            print("First Name: " + first_name + "-" + second_name)
        else:
            print("First Name: " + first_name)
        if second_surname != "":
            print("Surname: " + surname + " " + second_surname)
        else:
            print("Surname: " + surname)
    else:
        if second_name != "" and second_surname != "":
            print(f"{first_name}-{second_name} {surname} {second_surname}")
        elif second_name != "" and second_surname == "":
            print(f"{first_name}-{second_name} {surname}")
        elif second_name == "" and second_surname != "":
            print(f"{first_name} {surname} {second_surname}")
        else:
            print(f"{first_name} {surname}")


print_name("Charles", "Kane", second_surname="Addams", second_name="Bob", details=True)
