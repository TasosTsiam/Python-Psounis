#Πολύ καλύτερος και πιο neat τρόπος επίλυσης του καθηγητή, που εν μέρει σκέφτηκα μα δεν προσπάθησα
user_input = input("Enter your number: ")
while user_input != "quit":
    print(int(user_input) **2)
    user_input = input("Enter your Number: ")


#Τρόπος επίλυσης δικός μου. Δεν μου άρεσε, κι ας είναι σωστός.
number = True
while number:
    user_input = (input("Enter your number: "))
    if user_input == "quit":
        number = False
    else:
        print(int(user_input) ** 2)
