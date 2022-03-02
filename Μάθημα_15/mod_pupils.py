import json

pupils = []

# functions


def init_pupils_data():
    global pupils
    try:
        with open("pupils.json") as f:
            pupils = json.load(f)
    except FileNotFoundError:
        pupils = []


def save_pupils_data():
    with open("pupils.json", "w") as f:
        json.dump(pupils, f)


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
                age = int(age)
                p["Age"] = age
            else:
                print("Invalid input.")
                continue
        elif decision == "class":
            class_v = input("Update class: ")
            if class_v.strip().isdigit():
                class_v = int(class_v)
                p["Class"] = class_v
            else:
                print("Invalid input.")
                continue
        elif decision == "id number":
            id_number = input("Update id number: ")
            if id_number.strip().isdigit():
                id_number = int(id_number)
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


def delete_pupil_by_id(pupil_id):
    if type(pupil_id) is int:
        for p in pupils:
            if pupil_id == p["id"]:
                pupils.remove(p)
                my_string = f"Pupil with id: {pupil_id}, has been removed successfully!"
                return my_string
    elif type(pupil_id[0]) is dict:
        for p in pupils:
            for value in pupil_id[0].values():
                if value == p["id"]:
                    pupils.remove(p)
                    return

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
    if not pupils:
        return 1001
    else:
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
