N = 3

subsets = set()
subsets.add(frozenset())

for i in range(1, N + 1):
    new_subsets = set()
    for subset in subsets:
        non_frozen_set = set(subset)
        non_frozen_set.add(i)
        frozen_set = frozenset(non_frozen_set)
        new_subsets.add(frozen_set)
    subsets.update(new_subsets)

print(subsets)
print(len(subsets))
