import json

teachers = []

# functions


def init_teachers_data():
    global teachers
    try:
        with open("teachers.json") as f:
            teachers = json.load(f)
    except FileNotFoundError:
        teachers = []


def save_teachers_data():
    with open("teachers.json", "w") as f:
        json.dump(teachers, f)


def create_teacher(pump, auto):
    new_teacher = {}

    for t in teachers:
        if t["Name"] != pump or t["Surname"] != auto:
            teacher_id = input("Type id for this teacher: ")
            if teacher_id.strip().isdigit():
                teacher_id = int(teacher_id)
                for teacher in teachers:
                    for value in teacher.values():
                        if teacher_id == value:
                            print("This id is already used.")
                            print(teacher)
                            return

                new_teacher["teacher_id"] = teacher_id
            else:
                print("Invalid input.")
                return create_teacher(pump, auto)
            new_teacher["Name"] = pump
            new_teacher["Surname"] = auto
            teachers.append(new_teacher)
            print("Teacher has been added successfully!")
            print(teachers)
            return
        else:
            print("This teacher already exists.")
            print(t)
            return


def read_teacher():
    while True:
        teacher_id = input("Type id for this teacher: ")
        if teacher_id.strip().isdigit():
            teacher_id = int(teacher_id)
            for t in teachers:
                for value in t.values():
                    if value == teacher_id:
                        print(t)
                        return

            print("There's no teacher with this id. Try again!")
            continue
        else:
            print("Invalid input.")
            continue


def update_teacher():
    while True:
        teacher_id = input("Type id for this teacher: ")
        if teacher_id.strip().isdigit():
            teacher_id = int(teacher_id)
            for t in teachers:
                for value in t.values():
                    if value == teacher_id:
                        print(t)
                        while True:
                            choice1 = input("Which category do you want to update ('Name' = 1, 'Surname' = 2): ")
                            if choice1.strip().isdigit():
                                choice1 = int(choice1)
                                if choice1 == 1:
                                    while True:
                                        choice2 = input("Change 'Name': ")
                                        if choice2.strip().isalpha():
                                            t["Name"] = choice2
                                            print("Teacher's name has been updated successfully!")
                                            print(t)
                                            return
                                        else:
                                            print("Invalid input.")
                                            continue
                                elif choice1 == 2:
                                    while True:
                                        choice2 = input("Change 'Surname': ")
                                        if choice2.strip().isalpha():
                                            t["Surname"] = choice2
                                            print("Teacher's surname has been updated successfully!")
                                            print(t)
                                            return
                                        else:
                                            print("Invalid input.")
                                            continue
                                else:
                                    print("invalid input.")
                                    continue
                            else:
                                print("Invalid input.")
                                continue

            print("There's no teacher with this id. Try again!")
            continue
        else:
            print("Invalid input.")
            continue


def delete_teacher():
    while True:
        teacher_id = input("Type id for this teacher: ")
        if teacher_id.strip().isdigit():
            teacher_id = int(teacher_id)
            for t in teachers:
                for value in t.values():
                    if value == teacher_id:
                        print(t)
                        while True:
                            choice = input("Do you want to delete this teacher from the list? y-yes, n-no: ")
                            if choice.strip().isalpha():
                                if choice == "y":
                                    teachers.remove(t)
                                    print("Teacher has been removed successfully!")
                                    return
                                elif choice == "n":
                                    return delete_teacher()
                                else:
                                    print("Invalid input.")
                                    continue

                            else:
                                print("Invalid input.")
                                continue

            print("There's no teacher with this id. Try again!")
            continue
        else:
            print("Invalid input")
            continue
