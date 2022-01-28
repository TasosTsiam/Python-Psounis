# Δικός μου τρόπος επίλυσης
def float_average(*poggochampus):
    print(poggochampus)
    s = 0
    p = 0
    for pogchamp in poggochampus:
        print(pogchamp)
        s += pogchamp
        p += 1
    return s, p, s / p


print(f"float average = {float_average(2.1, 4.2, 5.9, 7.8)}")


# Τρόπος επίλυσης του Ψούνη, πιο απλός και κομψός, και νομίζω και πιο σωστός βάσει εκφώνησης.
def float_average2(*poggochampus2):
    print(poggochampus2)
    s = 0
    for pogchamp in poggochampus2:
        print(pogchamp)
        s += pogchamp
    return s / len(poggochampus2)


print(f"float average = {float_average2(2.1, 4.2, 5.9, 7.8)}")