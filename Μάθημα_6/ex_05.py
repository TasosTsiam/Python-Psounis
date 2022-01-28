#Κατασκευάστε μία λίστα που περιέχει τους άρτιους αριθμούς που είναι
#και πολλαπλάσια του 3, χρησιμοποιώντας για την κατασκευή, περιγραφική λίστα.

even_list = []
for even_number in range(100):
    if even_number % 2 == 0 and even_number % 3 == 0:
        even_list.append(even_number)
print(even_list)

even_list2 = [even_number for even_number in range(150) if even_number % 2 == 0 and even_number % 3 == 0]
print(even_list2)
