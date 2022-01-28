# Τρόπος υλοποίησης μου του αλγόριθμου του Ευκλίδη:


def euklidis(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
    p = a

    return p


print(euklidis(255, 155))


# Τρόπος υλοποίησης του Ψούνη, του αλγόριθμου του Ευκλίδη:
# Τον έκανε όπως πρέπει, με αναδρομική επίλυση, επικαλούμενος την συνάρτηση μέσα στην συνάρτηση.


def euclid(a, b):
    if a == b:
        return a
    elif a < b:
        return euclid(a, b - a)
    else:
        return euclid(b, a - b)


print(euclid(255, 155))