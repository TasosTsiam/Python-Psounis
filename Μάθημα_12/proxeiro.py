N = 1000

#global variables
pupils = [
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
        "Surname": "Green",
        "Fathers_name": "Beheheho",
        "Age": 22,
        "Class": 4,
        "id_number": "AN891005"
    }
]

# functions


def updating(p):
    while True:
        print("\nOnly small letters and space are allowed.")
        decision = input("Choose which section you want to update by typing the word: ")
        if decision == "name":
            p["Name"] = input("Update name: ").capitalize().strip()
            if not p["Name"].isalpha():
                print("Invalid input.")
                continue
        elif decision == "surname":
            p["Surname"] = input("Update surname: ").capitalize().strip()
            if not p["Surname"].isalpha():
                print("Invalid input.")
                continue
        elif decision == "fathers name":
            p["Fathers_name"] = input("Update father's name: ").capitalize().strip()
            if not p["Fathers_name"].isalpha():
                print("Invalid input.")
                continue
        elif decision == "age":
            age = input("Update age: ")
            if age.strip().isdigit():
                p["Age"] = age
            else:
                print("Invalid input.")
                continue
        elif decision == "class":
            class_v = input("Update class: ")
            if class_v.strip().isdigit():
                p["Class"] = class_v
            else:
                print("Invalid input.")
                continue
        elif decision == "id number":
            id_number = input("Update id number: ")
            if id_number.strip().isdigit():
                p["id_number"] = id_number
            else:
                print("Invalid input.")
                continue
        else:
            print("Invalid input.")
            return None
        break

    for key, value in p.items():
        print(f"{key.ljust(12)}: {value}")


def print_pupils_details():
    for p in pupils:
        print("")
        print_pupil(p)


def print_pupils_names():
    name = ""
    surname = ""
    fathers_name = ""
    for p in pupils:
        for key, value in p.items():
            if key == "Name":
                name = value
            if key == "Surname":
                surname = value
            if key == "Fathers_name":
                fathers_name = value[0]

        print("")
        print(name, fathers_name, surname)


def search_pupil_by_id(pupil_id):
    for p in pupils:
        if pupil_id == p["id"]:
            return p
    return None


def search_pupil_by_surname(surname):
    my_list = []
    for p in pupils:
        if surname == p["Surname"]:
            my_list.append(p)

    if len(my_list) > 0:
        return my_list
    else:
        return None


def print_pupil(pupil):
    print(f"Name         : {pupil['Name']}")
    print(f"Surname      : {pupil['Surname']}")
    print(f"Father's Name: {pupil['Fathers_name']}")
    print(f"Age          : {pupil['Age']}")
    print(f"Class        : {pupil['Class']}")
    if "id_number" in pupil:
        print(f"ID card number: {pupil['id_number']}")


def next_id():
    ids = []
    for p in pupils:
        ids.append(p["id"])
    return max(ids) + 1


def create_pupil():
    name = input("Give name: ")
    surname = input("Give surname: ")
    fathers_name = input("Give father's name: ")

    for p in pupils:
        if name == p["Name"] and surname == ["Surname"] and fathers_name == p["Fathers_name"]:
            print("This pupil already exists. ")
            ch = input("Do you want to continue? (y-yes, n-no): ")
            if ch == "n":
                return None

    age = int(input("Give age: "))
    pupil_class = int(input("Give class: "))
    id_card = input("Does he/she has an id card: (y-yes, n-no): ")
    if id_card == "y":
        id_number = input("Give id number: ")

    pupil = {}
    pupil["Name"] = name
    pupil["Surname"] = surname
    pupil["Fathers_name"] = fathers_name
    pupil["Age"] = age
    pupil["Class"] = pupil_class
    if id_card == "y":
        pupil["id_number"] = id_number

    pupil["id"] = next_id()

    pupils.append(pupil)
    return pupil


def main():
    while True:
        print("\n===============")
        print("      MENU")
        print("1 - Create Pupil")
        print("2 - Print")
        print("3 - Update Pupil")
        print("4 - Delete Pupil")
        print("5 - Exit")
        choice = input("Pick choice: ")
        if choice.strip().isdigit():
            choice = int(choice)
        else:
            print("Invalid input.")
            continue

        if choice == 1:
            print("New Pupil")
            print("===========")
            pupil = create_pupil()
            if pupil is None:
                continue
            else:
                print("New Pupil")
                print_pupil(pupil)
            print(pupils)

        elif choice == 2:
            print("1 - Print Pupil")
            print("2 - Print all pupils (analytically)")
            print("3 - Print all pupils (names only)")
            print("4 - Print pupils with certain surname")
            pupil_id = input("Pick choice: ")
            if pupil_id.strip().isdigit():
                pupil_id = int(pupil_id)
            else:
                print("Invalid input.")
                continue

            if pupil_id == 1:
                pupil_id = int(input("Type pupil's id: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil with this id does not exist.")
                else:
                    print("    Pupil    ")
                    print_pupil(pupil)

            elif pupil_id == 2:
                print_pupils_details()
            elif pupil_id == 3:
                print_pupils_names()
            elif pupil_id == 4:
                pupil_surname = input("Type a specific surname: ")
                pupil_2 = search_pupil_by_surname(pupil_surname)
                if pupil_2 is None:
                    print("Pupil with this surname does not exist.")
                else:
                    print("   Pupil    ")
                    print(pupil_2)

            else:
                print("Invalid input.")
                continue

        elif choice == 3:
            print("1 - Search pupil by Surname")
            print("2 - Search pupil by id")
            choice_3 = input("Pick choice: ")
            if choice_3.strip().isdigit():
                choice_3 = int(choice_3)
            else:
                print("Invalid input.")
                continue
            if choice_3 == 1:
                pupil_surname = input("Type a specific surname: ")
                pupil_2 = search_pupil_by_surname(pupil_surname)
                if pupil_2 is None:
                    print("Pupil with this surname does not exist.")
                    continue
                else:
                    print("   Pupil    ")
                    print(pupil_2)

                if len(pupil_2) > 1:
                    check = True
                    pupil_id = input("Type a pupil's id to update the specific pupil: ")
                    if pupil_id.strip().isdigit():
                        pupil_id = int(pupil_id)
                    else:
                        print("Invalid input.")
                        continue
                    for p in pupils:
                        if pupil_id == p["id"]:
                            print(p)
                            updating(p)
                            check = False
                            break

                    if check:
                        print("Pupil with this id does not exist. ")
                        continue

            elif choice_3 == 2:
                pupil_id = int(input("Type a pupil's id to update the specific pupil: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil with this id does not exist.")
                else:
                    print("    Pupil    ")
                    print_pupil(pupil)
                    for p in pupils:
                        if pupil_id == p["id"]:
                            updating(p)
            else:
                print("Invalid input.")
                continue

        elif choice == 4:
            pass
        elif choice == 5:
            print("Bye bye!")
            quit()
        else:
            print("Invalid input. Please choose either '1', '2', '3', '4', or '5'.")
            continue


main()
