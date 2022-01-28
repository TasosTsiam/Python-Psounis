N = 5
set = set()

for i in range(1, N + 1):
    for j in range(i +1, N + 1):
        set.add(frozenset({i, j}))
print(set)
