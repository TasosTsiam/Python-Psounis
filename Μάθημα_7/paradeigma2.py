A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

#print(A | B)
#print(A.union(B))

#print(A & B)
#print(A.intersection(B))

#print(B.difference(A))
#print(A - B)

#print(A ^ B)
#print(A.symmetric_difference(B))


#print(A.issubset(B))
#print(A.issuperset(B))
#print(A.isdisjoint(B))

#A.update(B)
#print(A)

#A.intersection_update(B)
#print(A)

#A.difference_update(B)
#print(A)

A.symmetric_difference_update(B)
print(A)
