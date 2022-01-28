N = 1000
K = 1
pupils_list = [
    {
        "pupil1" :
        {"id" : 1001,
        "Name" : "Alice",
        "Surname" : "Cullen",
        "Fathers_name" : "Carlisle",
        "Age" : 20,
        "Class" : 2,
        "id_number" : "AN342034"}
    },
    {
        "pupil2" :
        {"id" : 1002,
        "Name" : "Ashley",
        "Surname" : "Green",
        "Fathers_name" : "John",
        "Age" : 21,
        "Class" : 3,
        "id_number" : "AN550760"}
    },
    {
        "pupil3" :
        {"id" : 1003,
        "Name" : "Evelyn",
        "Surname" : "Lolen",
        "Fathers_name" : "Beheheho",
        "Age" : 22,
        "Class" : 4,
        "id_number" : "AN891005"}
    }
]

print("1) Create Account")
print("2) Print")
print("3) Account settings")
print("4) Delete Account")
print("5) Exit")

print("")
print(type(pupils_list[2]))
while True:
    user_choice = int(input("Pick your choice: "))

    if user_choice == 1:
        pupil_name = input("Insert name: ")
        pupil_surname = input("Insert surname: ")
        pupil_fathers_name = input("Insert father name: ")

        for i in pupils_list:
            i = list(i)
            for j in i:
                if pupil_name in j or pupil_surname in j or pupil_fathers_name in j:
                    print(f"""Pupil already exists. Details :
                             {pupils_list[i]}""")
                    v1 = input("""Is this a different pupil?
                                  'yes' or 'no': """)
                    if v1 == "yes":
                        print("Continuing with submission...")
                        break
                    elif v1 == "no":
                        print("Cancelling this submission...")
                        continue

        pupil_age = input("Insert age: ")
        pupil_class = input("Insert Class between 1-6: ")
        pupil_id_number = input("Insert id number. If there's no id, type 'None': ")

        pupils_list.append({f"pupil{len(pupils_list) + 1}" :
        {"id" : N + len(pupils_list) + 1,
         "Name" : pupil_name,
         "Surname" : pupil_surname,
         "Fathers_name" : pupil_fathers_name,
         "Age" : pupil_age,
         "Class" : pupil_class,
         "id_number" : pupil_id_number}}
         )
#    elif user_choice == 2:


#    elif user_choice == 3:
        pupil_name = input("Update name: ")
        pupil_surname = input("Update surname: ")
        pupil_fathers_name = input("Update father name: ")
        pupil_age = input("Update age: ")
        pupil_class = input("Update Class between 1-6: ")
        pupil_id_number = input("Update id number. If there's no id, type 'None': ")
#    elif user_choice == 4:

    elif user_choice == 5:
        print("Bye bye!")
        quit()
