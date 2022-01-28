#Ολόσωστο execution και πρόγραμμα, αρκετά advanced και πιο λειτουργικό απ' την εκφώνηση και τα όσα μάθαμε'
#Ξεκάθαρα, ο λόςο πάλι, είναι ότι γνωρίζω ήδη. Πέραν αυτού, δεν είχα σκεφτεί να εφαρμόσω boolean operators(σχεσιακούς τελεστές)
#Δηλαδή, το έλυσε ο καθηγητής ρωτώντας στο "if" αν η v1 > v2 --and-- v1 > v3 κλπ κλπ.
v1 = int(input("Enter your Number: "))
v2 = int(input("Enter your Number: "))
v3 = int(input("Enter your Number: "))
if v1 > v2:
    if v1 > v3:
        print(str(v1) + " is the largest number!")
    elif v1 == v3:
        print("No number stands above all the others.")
    else:
        print(str(v3) + " is the largest number!")
elif v2 > v1:
    if v2 > v3:
        print(str(v2) + " is the largest number!")
    elif v2 == v3:
        print("No number stands above all the others.")
    else:
        print(str(v3) + " is the largest number!")
else:
    print("No number stands above the all the others.")
