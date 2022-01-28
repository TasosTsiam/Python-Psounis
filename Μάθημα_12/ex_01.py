# Τρόπος επίλυσης παραγοντικού αριθμού μέσω recursive function


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(1, 11):
    print(f"factorial({i}) = {factorial(i)}")


# Τρόπος επίλυσης παραγοντικού αριθμού μέσω επαναληπτικής for loop


def factorial2(n):
    p = 1
    for i in range(2, n + 1):
        p = p * i

    return p


for i in range(1, 11):
    print(f"factorial({i}) = {factorial2(i)}")
