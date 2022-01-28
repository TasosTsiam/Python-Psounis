print("You only have 10 attempts, good luck!")
hidden_number = 15
maximum_attempts = 10
user_attempts = 0
while user_attempts < maximum_attempts:
    user_input = int(input("Enter your number: "))
    user_attempts += 1
    if user_input < 15:
        print("Your number is less than the hidden number.")
    elif user_input > 15:
        print("Your number is greater than the hidden number.")
    else:
        print("Congratsulations, you've found the hidden number!")
        break
    if user_attempts == maximum_attempts:
        print("You lost. You've reached the maximum attempts. Good luck next time!")
