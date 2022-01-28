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
        "Surname": "Lolen",
        "Fathers_name": "Beheheho",
        "Age": 22,
        "Class": 4,
        "id_number": "AN891005"
    }
]

#functions


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


def print_pupil(pupil):
    print(f"Name : {pupil['Name']}")
    print(f"Surname : {pupil['Surname']}")
    print(f"Father's Name : {pupil['Fathers_name']}")
    print(f"Age : {pupil['Age']}")
    print(f"Class : {pupil['Class']}")
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
        choice = int(input("Pick one: "))

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
            choice_2 = input("Pick one: ")
            if choice_2.strip().isdigit():
                choice_2 = int(choice_2)
            else:
                print("Invalid input.")
                continue

            if choice_2 == 1:
                pupil_id = int(input("Type pupil's id: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil with this id does not exist.")
                else:
                    print("    Pupil    ")
                    print_pupil(pupil)


            elif choice_2 == 2:
                print_pupils_details()
            elif choice_2 == 3:
                print_pupils_names()
            else:
                print("Invalid input. To choose, type either '1', '2', or '3'.")
                continue

        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Bye bye!")
            quit()


main()