#Τρόπος δικός μου!
N = 20
for i in range(0, N):
    for j in range(0, N - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    for j in range(0, i):
        print("*", end="")
    print("")


#Τρόπος του καθηγητή, που χρησιμοποίησε μαθηματικό τύπο για τους μονούς αριθμούς
N = 20
for i in range(0, N):
    for j in range(0, N - i - 1):
        print(" ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    print("")

#Το παράδειγμα όταν το πρωτοείδαμε. 
N = 20
for i in range(0, N):
    for j in range(0, N - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("*", end="")
