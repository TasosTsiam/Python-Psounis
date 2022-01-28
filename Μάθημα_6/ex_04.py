#Πρώτοι αριθμοί
#Κατασκευάστε ένα πρόγραμμα το οποίο:
#1) Θα κατασκευάζει και θα τυπώνει ένα tuple με τους πρώτους
#   αριθμούς που θα υπάρχουν από το 2 έως το 100.

primal_list = []
for x in range(2, 100 + 1):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        primal_list.append(x)
primal_tuple = tuple(primal_list)
print(primal_tuple)
