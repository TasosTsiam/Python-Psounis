user_input = int(input("Enter the amount of attempts, between 3 and 20: "))
while user_input < 3 or user_input > 20:
    user_input = int(input("Invalid number. Enter a number between 3 and 20: "))

numbers = []
for count in range(0, user_input):
    if count == 0:
        numbers.append(int(input("Enter " + str(count + 1) + "st number: ")))
    elif count == 1:
        numbers.append(int(input("Enter " + str(count + 1) + "nd number: ")))
    elif count == 2:
        numbers.append(int(input("Enter " + str(count + 1) + "rd number: ")))
    else:
        numbers.append(int(input("Enter " + str(count + 1) + "th number: ")))
numbers.sort()
print(numbers)
