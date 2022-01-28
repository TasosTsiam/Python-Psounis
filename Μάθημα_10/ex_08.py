N = 1000
pupils_list = [
    {
        "id": 1001,
        "Name": "Alice",
        "Surname": "Cullen",
        "Fathers_name": "Carlisle",
        "Age": 20,
        "Class": 2,
        "id_number": "AN342034"
    },
    {
        "id": 1002,
        "Name": "Ashley",
        "Surname": "Green",
        "Fathers_name": "John",
        "Age": 21,
        "Class": 3,
        "id_number": "AN550760"
    },
    {
        "id": 1003,
        "Name": "Evelyn",
        "Surname": "Lolen",
        "Fathers_name": "Beheheho",
        "Age": 22,
        "Class": 4,
        "id_number": "AN891005"
    }
]


while True:
    print("--------------------")
    print("1) Create Account")
    print("2) Print")
    print("3) Account settings")
    print("4) Delete Account")
    print("5) Exit")

    user_choice = int(input("Pick your choice: "))

    if user_choice == 1:
        pupil_name = input("Insert name: ")
        pupil_surname = input("Insert surname: ")
        pupil_fathers_name = input("Insert father name: ")

        stop = False

        for i in pupils_list:
            if i['Name'] == pupil_name and i['Surname'] == pupil_surname and i['Fathers_name'] == pupil_fathers_name:

                print(f"\nPupil already exists. \nDetails :")
                for key, value in i.items():
                    print(f"\t{key.ljust(12)} : {value}")
                print("")
                user_choice2 = input("""Is this a different pupil?\n'yes' or 'no': """)

                if user_choice2 == "yes":
                    print("Continuing with submission...")
                    print("")
                    break

                elif user_choice2 == "no":
                    print("Cancelling this submission...")
                    print("")
                    stop = True
                    break

        if stop == True:
            continue

        pupil_age = input("Insert age: ")
        pupil_class = input("Insert Class between 1-6: ")
        pupil_id_number = input(
            "Insert id number. If there's no id, type 'None': ")

        pupils_list.append({
            "id": N + len(pupils_list) + 1,
            "Name": pupil_name,
            "Surname": pupil_surname,
            "Fathers_name": pupil_fathers_name,
            "Age": pupil_age,
            "Class": pupil_class,
            "id_number": pupil_id_number
        })
        print("")
        print("You've submitted the new pupil with success!")
        print("")
        for i in pupils_list:
            if i == pupils_list[-1]:
                for key, value, in i.items():
                    print(f"{key.ljust(12)} : {value}")
        print("")



#    elif user_choice == 2:
#        print(pupils_list)
#    elif user_choice == 3:
#        pupil_name = input("Update name: ")
#        pupil_surname = input("Update surname: ")
#        pupil_fathers_name = input("Update father name: ")
#        pupil_age = input("Update age: ")
#        pupil_class = input("Update Class between 1-6: ")
#        pupil_id_number = input(
#            "Update id number. If there's no id, type 'None': ")
#    elif user_choice == 4:
#        print('coming soon')
    elif user_choice == 5:
        print("Bye bye!")
        quit()
