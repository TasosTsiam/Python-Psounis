# Τρόπος επίλυσης μου, που αποδείχθηκε από απάντηση Ψούνη ότι είναι πάρα πολύ ωραίος, και μπροστά, συγκριτικά με αυτά
# που μέχρι τώρα γνωρίζω
my_list = []


def fibonacci(n):
    global my_list
    if n == 0:
        my_list.append(n)
        return 0
    elif n == 1:
        my_list.append(n)
        return 1
    else:
        n = my_list[-1] + my_list[-2]
        my_list.append(n)
        return n


for i in range(101):
    print(f"fibonacci({i}) = {fibonacci(i)}")


# Τρόπος επίλυσης του Ψούνη.


def fibonacci(n):
    fib = [1, 2]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


for i in range(101):
    print(f"fibonacci({i}) = {fibonacci(i)}")