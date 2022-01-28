my_int = 10
my_float = 5.5
my_string = "Hello!"

print(str(my_int) + " and " +  str(my_float) + " and " + my_string)
print(f"{my_int} and {my_float} and {my_string}")
print("%d and %.1f and %s" % (my_int, my_float, my_string))
print("{} and {} and {}".format(my_int, my_float, my_string))
