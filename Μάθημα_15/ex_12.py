import json
from mod_pupils import *
from mod_teachers import *


def main():
    init_teachers_data()
    init_pupils_data()
    while True:
        print("\n=================")
        print("      MENU")
        print(" Pupil Area:")
        print("1 - Create Pupil")
        print("2 - Print Pupil")
        print("3 - Update Pupil")
        print("4 - Delete Pupil")
        print("      -      \nTeachers Area:")
        print("5 - Create Teacher")
        print("6 - Print Teacher")
        print("7 - Update Teacher")
        print("8 - Delete Teacher")
        print("      - \n9 - Exit")
        print("")
        choice = input("Pick choice: ")
        if choice.strip().isdigit():
            choice = int(choice)
        else:
            print("Invalid input.")
            continue

        if choice == 1:
            init_pupils_data()
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
            init_pupils_data()
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
            init_pupils_data()
            print("1 - Delete pupil by Surname")
            print("2 - Delete pupil by id")
            choice_4 = input("Pick choice: ")
            if choice_4.strip().isdigit():
                choice_4 = int(choice_4)
            else:
                print("Invalid input.")
                continue
            if choice_4 == 1:
                pupil_surname = input("Type a specific surname: ")
                pupil_4 = search_pupil_by_surname(pupil_surname)
                if pupil_4 is None:
                    print("Pupil with this surname does not exist.")
                    continue
                else:
                    print("   Pupil    ")
                    print(pupil_4)
                if len(pupil_4) > 1:
                    pupil_id = input("Type a pupil's id to delete the specific pupil: ")
                    if pupil_id.strip().isdigit():
                        pupil_id = int(pupil_id)
                        pupil = delete_pupil_by_id(pupil_id)
                        if pupil is None:
                            print("Pupil with this id does not exist.")
                        else:
                            print(pupil)
                    else:
                        print("Invalid input.")
                        continue
                else:  # len(pupil_4) <= 1
                    print("Deleting this pupil...")
                    delete_pupil_by_id(pupil_4)
                    print(pupils)

            elif choice_4 == 2:
                pupil_id = input("Type a pupil's id to delete the specific pupil: ")
                if pupil_id.strip().isdigit():
                    pupil_id = int(pupil_id)
                    pupil = delete_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Pupil with this id does not exist.")
                    else:
                        print(pupil)
            else:
                print("Invalid input.")
                continue

        elif choice == 5:
            while True:
                name = input("Type name: ")
                if name.strip().isalpha():
                    pass
                else:
                    print("Invalid input.")
                    continue
                surname = input("Type surname: ")
                if surname.strip().isalpha():
                    pass
                else:
                    print("Invalid input.")
                    continue
                create_teacher(name, surname)
                break

        elif choice == 6:
            read_teacher()
        elif choice == 7:
            update_teacher()
        elif choice == 8:
            delete_teacher()
        elif choice == 9:
            print("Bye bye!")
            save_pupils_data()
            save_teachers_data()
            quit()
        else:
            print("Invalid input. Please choose either '1', '2', '3', '4', or '5'.")
            continue


main()
