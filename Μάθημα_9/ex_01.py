from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

array = []

for row in range(3):
    new_row = []
    for item in range(3):
        new_row.append(randrange(0, 1000))
    array.append(new_row)

for row in array:
    for i in range(3):
        print("+----", end="")
    print("+")
    for item in row:
        print(("|" + str(item) + "\t").expandtabs(5), end="")
    print("|")
for i in range(3):
    print("+----", end="")
print("+")
