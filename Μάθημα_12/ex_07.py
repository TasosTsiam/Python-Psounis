def c(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    else:
        return c(n - 1, k - 1) + c(n - 1, k)


print(c(49, 6))