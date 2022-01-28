# Τρόπος Ψούνη

def binary_search2(array, x, start, finish):
    middle = (start + finish) // 2

    if start <= finish:
        if x == array[middle]:
            return middle
        elif x < array[middle]:
            return binary_search2(array, x, start, middle - 1)
        else:  # x > array[middle]
            return binary_search2(array, x, middle + 1, finish)
    else:
        return -1


my_list2 = [i * i for i in range(10)]
print(my_list2)
print(binary_search2(my_list2, 9, 0, len(my_list2) - 1))

# Τρόπος δικός μου


def binary_search(my_list):
    global n
    k = (len(my_list) - 1) // 2
    x = my_list[k]
    print(my_list)
    print(x)

    if n == x:
        return x
    elif n > x:
        return binary_search(my_list[k + 1:])
    else:
        return binary_search(my_list[:k])


n = 225

print(binary_search([i * i for i in range(4, 21)]))
