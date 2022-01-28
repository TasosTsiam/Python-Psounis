merchandise = {
    "book" : 10.18,
    "Μαϊντανός" : 0.22,
    "Τσιμέντο" : 5.17,
    "CD" : 0.05
}

rate = 2.2
new_values = {key : value * rate for key, value in merchandise.items()}

print(new_values)
