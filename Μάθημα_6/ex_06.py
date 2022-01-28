#Κατασκευάστε μία λίστα που απεικονίζει έναν 3χ4 πίνακα (με στοιχεία της επιλογής σας) και έπειτα:
# 1) Προσθέτει μία γραμμή μηδενικών στην αρχή
# 2) Τυπώνει τον 4χ4 πίνακα.
# 3) Προσθέτει μία στήλη με άσσους στο τέλος
# 4) Τυπώνει τον 4χ5 πίνακα

my_list = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10 ,11, 12]
]
my_list.insert(0, [0, 0, 0, 0])
for row in my_list:
    for elem in row:
        print(elem, end=" ")
    print("")
for row in my_list:
    row.append(1)
print("")
for row in my_list:
    for elem in row:
        print(elem, end=" ")
    print("")
