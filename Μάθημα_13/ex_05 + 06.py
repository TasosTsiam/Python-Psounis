# Άσκηση 5) όπου υλοποιούμε τον αλγόριθμο ταξινόμησης με επιλογή (selection sort)
# Άσκηση 6) όπου χρησιμοποιούμε ακριβώς την ίδια συνάρτηση, προσθέτοντας παράμετρο
# που θα καθορίζει αν θα ταξινομείται με αύξουσα ή φθίνουσα σειρά.
def selection_sort(array, par2=False):
    if par2:
        for i in range(0, len(array)):
            pos = i
            for j in range(i + 1, len(array)):
                if array[j] > array[pos]:
                    pos = j

            array[i], array[pos] = array[pos], array[i]
    else:
        for i in range(0, len(array)):
            pos = i
            for j in range(i+1, len(array)):
                if array[j] < array[pos]:
                    pos = j

            array[i], array[pos] = array[pos], array[i]


array = [1, 5, 2, 8, 4, 7, 3, 9, 6]
selection_sort(array)
print(array)
selection_sort(array, par2=True)
print(array)
