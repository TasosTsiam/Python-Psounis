from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

zaries = {1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0}

mutable_Όφις = 1000000
for i in range(mutable_Όφις):
    i = randrange(1, 7)
    zaries[i] += 1
print(zaries)

for i in range(1, 7):
    pososto_zarias = (zaries[i] / mutable_Όφις) * 100
    print("Το ζάρι " + str(i) + " έτυχε " + str(pososto_zarias) + "%")
