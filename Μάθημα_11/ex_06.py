PI = 3.14159265359

def triangle_area(base, height):
    return (base * height) / 2
def square_perimeter(edge):
    return edge * 4
def square_area(edge):
    return edge ** 2
def circle_perimeter(radius):
    return 2 * PI * radius
def circle_area(radius):
    return PI * (radius ** 2)


print(triangle_area(10, 40))
print(square_perimeter(5))
print(square_area(5))
print(circle_perimeter(5))
print(circle_area(5))
