#Πολύ ενδιαφέρον το γεγονός ότι με τον τρόπο που σκέφτηκα, δημιουργώ ένα loop
#χωρίς να χρησιμοποιώ κάποια while / for κλπ.
#Ο Ψούνης έκανε την άσκηση με while, χωρίς να χρησιμοποιεί 2η φορά την συνάρτηση,
#μέσα στην συνάρτηση. Sounds weird but I like it!

#1ος τρόπος που βρήκα, με return

def input_integer():
    user_input = input("Type an integer: ").strip()
    if user_input.isdigit():
        user_input = int(user_input)
        print(user_input)
        return
#    else:
    print("Invalid input.")
    input_integer()

input_integer()

#2ος τρόπος που βρήκα, με else
def input_integer():
    user_input = input("Type an integer: ").strip()
    if user_input.isdigit():
        user_input = int(user_input)
        print(user_input)
#        return
    else:
        print("Invalid input.")
        input_integer()

input_integer()

#3ος τρόπος που βρήκα, και με return, και με else
def input_integer():
    user_input = input("Type an integer: ").strip()
    if user_input.isdigit():
        user_input = int(user_input)
        print(user_input)
        return
    else:
        print("Invalid input.")
        input_integer()

input_integer()
