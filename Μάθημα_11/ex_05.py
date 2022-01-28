def is_odd(number):
    return number % 2 == 1
def is_even(number):
    return number % 2 == 0
def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True
def is_square(number):
    for i in range(n + 1):
        if i * i == number:
            return True
    return False

def is_cube(number):
    for i in range(n + 1):
        if i ** 3 == number:
            return True
    return False

n = 100

for i in range(1, n + 1):
    print(f"\nis {i} odd?\t = {is_odd(i)}\nis {i} even?\t = {is_even(i)}\nis {i} prime?\t = {is_prime(i)}\nis {i} square?\t = {is_square(i)}\nis {i} cube?\t = {is_cube(i)}")
