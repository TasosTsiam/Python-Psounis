duplicates = {1, 5, 2, 4, 4, 3, 2, 1, 2, 1}
print(duplicates)


empty_set = set()
print(type(empty_set))


list1 = [1, 2, 3]
list2 = list1
list2[0] = 4
print(list1,"\n",list2)


set1 = {1, 2, 3, 4}
set2 = set1.copy()
set2.add(5)

print(set1, set2)
