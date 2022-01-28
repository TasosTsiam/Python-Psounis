def print_list(list):
    if len(list) > 0:
#        print(list)
        print(list[0], end= " ")
        print(list)
        print_list(list[1:])
#        print(list)


def print_list2(list):
    if len(list) > 0:
#        print(list)
        print_list2(list[1:])
        print(list)
        print(list[0], end= " ")
#        print(list)


print_list([1, 2, 3, 4, 5])
print("")
print_list2([1, 2, 3, 4, 5])