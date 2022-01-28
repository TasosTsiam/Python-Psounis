def f(arg):
    print(arg)
    print(id(arg))
    arg = "Change!"
    print(id(arg), arg)


s = "Initial"
print(s)
print(id(s))
f(s)
print(s)
print(id(s))
print("")

def f(arg):
    print(id(arg), arg)
    arg.append(3)
    print(id(arg), arg)


list = [1, 2]
print(id(list), list)
f(list)
print(id(list), list)
print("")

def f(arg):
    print(id(arg), arg)
    arg = [3]
    print(id(arg), arg)


list = [1, 2]
print(id(list), list)
f(list)
print(id(list), list)
