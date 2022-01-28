#Δυναμική κατασκευή tuples
#Για κάποιους μυστήριους λόγους θέλουμε να κατασκευάσουμε
#ένα πρόγραμμα το οποίο :
#1) Θα διαβάζει από την είσοδο 10 ακέραιους μεταξύ 10 και 20 και θα
#   τους αποθηκεύει σε μία λίστα.
#2) Θα δημιουργεί ένα tuple με περιεχόμενο αυτούς τους 10 αριθμούς.
#3) Θα δημιουργεί ένα δεύτερο tuple το οποίο θα περιέχει ταξινομημένα
#   τα τετράγωνα αυτών των 10 αριθμών.


print("Only numbers between 10 and 20")
list = []
for i in range(10):
    user_input = int(input("Enter your number: "))
    while user_input < 10 or user_input > 20:
        user_input = int(input("Enter a number between 10 and 20: "))
    list.append(user_input)
tuple = tuple(list)
list_squares = []
for i in range(10):
    list_squares.append(list[i] ** 2)
list_squares.sort()
tuple_squares = list_squares
print(tuple_squares)
