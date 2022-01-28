int_list = [111, 2, 6, 15, 32, 600, 7, 8, 51, 11]
count = 1
biggest_so_far = int_list[0]
while count < len(int_list):
    if int_list[count] > biggest_so_far:
        biggest_so_far = int_list[count]
    count += 1
print(biggest_so_far)
