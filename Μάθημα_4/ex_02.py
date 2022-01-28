#Το έλυσα με τον παρακάτω τρόπο:
num_list = [39, 25, 40]
if num_list[0] > num_list[1] and num_list[0] > num_list[2]:
    print(num_list[0])
elif num_list[1] > num_list[0] and num_list[1] > num_list[2]:
    print(num_list[1])
else:
    print(num_list[2])

#Όμως, αυτός είναι ο τρόπος που το έλυσε ο καθηγητής, και είναι ωφέλιμος να τον συνηθίσω, ως αλγόριθμο:
num_list = [39, 25, 40]
maximum = num_list[0]
if num_list[1] > maximum:
    maximum = num_list[1]
if num_list[2] > maximum:
    maximum = num_list[2]
print(maximum)
