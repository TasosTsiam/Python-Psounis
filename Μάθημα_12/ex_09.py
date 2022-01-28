def binary_search(my_list):
    global n
    while True:
        k = (len(my_list) - 1) // 2
        x = my_list[k]
        print(my_list)
        print(x)
        if n == x:
            return x
        elif n > x:
            my_list = my_list[k + 1:]
            continue
        else:
            my_list = my_list[:k]
            continue


n = 13

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
