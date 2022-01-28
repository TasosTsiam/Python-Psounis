#Τρόπος με τον οποίο το έλυσα εγώ:

def digits_print(number):
    srt_number = str(number)
    if srt_number.isdigit():
        list_number = list(srt_number)
        first = list_number[0]
        second = list_number[1]
        third = list_number[2]
        print(f"1st digit: {first}\n2nd digit: {second}\n3rd digit: {third}")
    else:
        return None


print(digits_print(462))






#Πολύ ωραίος τρόπος με τον οποίο το έλυσε ο Ψούνης,
#Δείχνοντας μας μια νέα αλγορυθμική λογική με το % που πρέπει να προσθέσουμε στο μυαλό.

def digits_print2(number):
    third = number % 10
    number = number // 10
    second = number % 10
    first = number // 10
    print(f"1st digit: {first}\n2nd digit: {second}\n3rd digit: {third}")


digits_print(536)

def digits(number):
    if number < 100 or number > 999:
        return None
    else:
        third = number % 10
        number = number // 10
        second = number % 10
        first = number // 10
        return first, second, third


print(digits(446.3))
