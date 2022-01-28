#Η άσκηση που μου ζήτησε να κάνω είναι αρκετά πιο απλή, χωρίς να χρειάζεται το elif
#Μα επειδή το ξέρω ήδη από προηγούμενο course, το έκανα, ξέροντας ότι είναι advanced και πολύ καλύτερο.
v1 = int(input("Enter your Number: "))
v2 = int(input("Enter your Number: "))
if v1 > v2:
    print(str(v1) + " is the biggest number, champ!")
elif v1 < v2:
    print(str(v2) + " is the biggest number, fam!")
else:
    print(str(v1) + " == " + str(v2) + "\n""In other words, the numbers you've put are equal, dawg!")
