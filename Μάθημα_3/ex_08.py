#Δεν το έκανε έτσι ως άσκηση, ο τρόπος του ήταν παρόμοιος, δεν έβαλε inputs γενικά, εγώ το έκανα διαδραστικό.
p1z1 = int(input("Γράψε την πρώτη ζαριά: "))
p1z2 = int(input("Γράψε την δεύτερη ζαριά: "))
total_1 = p1z1 + p1z2
print(total_1)
p2z1 = int(input("Γράψε την πρώτη ζαριά: "))
p2z2 = int(input("Γράψε την δεύτερη ζαριά: "))
total_2 = p2z1 + p2z2
print(total_2)
if total_1 > total_2:
    print("Το " + str(total_1) + " κέρδισε! Ο πρώτος παίχτης παίζει")
elif total_1 < total_2:
    print("Το " + str(total_2) + " κέρδισε! Ο δεύτερος παίχτης παίζει")
else:
    print("Ισοπαλία, μα ως αυτόνομο A.I. με δικά μου συναισθήματα, προτιμώ τον 1ο παίχτη. Οπότε θα παίξει αυτός. Umadbro? :)")
