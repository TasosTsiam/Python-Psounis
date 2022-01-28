# Κατασκευή εξάδων στο ΛΟΤΤΟ
#Κατασκευάστε πρόγραμμα που θα επιλέγει τυχαίες 6-άδες του ΛΟΤΤΟ
#με τις ιδιότητες:
# 1) Δύο από τους αριθμούς θα είναι στο εύρος από 10-19
# 2) Δύο από τους αριθμούς θα είναι στο εύρος από 20-39
# 3) Ένας αριθνμός θα είναι ζυγός στο εύρος 1-9
# 4) Ένας αριθμός θα είναι μονός στο εύρος 40-49
# Το πρόγραμμα να κατασκευάζει 10 τέτοιες τυχαίες 6-άδες και να τις τυπώνει.

from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 10
for lotto_counts in range(1, N + 1):
    column = set()
    rand_number1 = randrange(10, 20)
    column.add(rand_number1)
    rand_number2 = randrange(10, 20)
    if rand_number2 != rand_number1:
        column.add(rand_number2)
    else:
        for i in range(10, 20):
            rand_number2 = randrange(10, 20)
            if rand_number2 != rand_number1:
                column.add(rand_number2)
                break
    rand_number3 = randrange(20, 40)
    column.add(rand_number3)
    rand_number4 = randrange(20, 40)
    if rand_number4 != rand_number3:
        column.add(rand_number4)
    else:
        for j in range(20, 40):
            rand_number4 = randrange(20, 40)
            if rand_number4 != rand_number3:
                column.add(rand_number4)
                break
    rand_number5 = randrange(1, 10)
    if rand_number5 % 2 == 0:
        column.add(rand_number5)
    else:
        for k in range(1, 10):
            if k % 2 == 0:
                column.add(rand_number5)
    rand_number6 = randrange(40, 50)
    if rand_number6 % 2 == 1:
        column.add(rand_number6)
    else:
        for z in range(40, 50):
            if z % 2 == 1:
                column.add(rand_number6)
    print(column)

#5, 5, 6, 5, 6, 3, 5, 4, 6, 4
