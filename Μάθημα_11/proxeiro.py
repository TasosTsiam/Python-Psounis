def square(x):
    return x * x


def cube(x):
    return x ** 3


def f(x):
    return 3 * cube(x) + 4 * square(x) + x + 1


x = 5
print(f(x))