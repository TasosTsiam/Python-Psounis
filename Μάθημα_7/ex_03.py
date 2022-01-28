#Σύνολα Αριθμών
#Κατασκευάστε τα εξής σύνολα φυσικών:
# 1) Το σύνολο των άρτιων από το 0 έως το 100.
# 2) Το σύνολο των περιττών από το 0 έως το 100.
# 3) Τα πολλαπλάσια του 3 από το 0 έως το 100.
# 4) Το σύνολο των πρώτων από το 0 έως το 100(Βλ. και μάθημα 6, ex_04)
# Τυπώστε τα περιεχόμενα τους, καθώς και το πλήθος
# των στοιχείων κάθε συνόλου.

N = 100
even100_set = set()
odd100_set = set()
multiple3_set = set()
prime100_set = set()
for number in range(N + 1):
    if number % 2 == 0:
        even100_set.add(number)
    if number % 2 == 1:
        odd100_set.add(number)
    if number % 3 == 0:
        multiple3_set.add(number)
    for number in range(2, N + 1):
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            prime100_set.add(number)

print(str(even100_set) + "\n" + str(odd100_set) +"\n"
+ str(multiple3_set) + "\n" + str(prime100_set))
print("")
print("Even_numbers set has: " "\n" + str(len(even100_set)) + " elements.")
print("")
print("Odd_numbers set has: " "\n" + str(len(odd100_set)) + " elements.")
print("")
print("Multiple_3_numbers set has: " "\n" + str(len(multiple3_set)) + " elements.")
print("")
print("Prime_numbers set has: " "\n" + str(len(prime100_set)) + " elements.")
print("")

#Πρέπει να τυπώσουμε τα σύνολα που είναι και even και multiples of 3.
set1 = even100_set | multiple3_set
print(set1)
print("")

#Πρέπει να τυπώσουμε ένα σύνολο που απαρτίζεται από τα
#κοινά στοιχεία των συνόλων των περιττών και πρώτων αριθμών.
set2 = odd100_set & prime100_set
print(set2)
print("")

#Πρέπει να τυπώσουμε ένα σύνολο πρώτων αριθμών που δεν είναι περιττοί.
set3 = prime100_set - odd100_set
print(set3)
print("")

#Πρέπει να τυπώσουμε ένα σύνολο που να εμπεριέχει είτε περιττούς,
#είτε πρώτους, αλλά όχι και περιττούς και πρώτους.
set4 = odd100_set.symmetric_difference(prime100_set)
print(set4)
