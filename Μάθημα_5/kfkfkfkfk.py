secret_number = 7
cnt = 0
guess_number = int(input("You have 10 chances! Guess the secret number: "))
while guess_number != secret_number:
    cnt += 1
    if cnt < 10:
        if guess_number < secret_number:
            guess_number = int(input("You have another chance. The secret number is bigger: "))
        else:
            guess_number = int(input("You have another chance. The secret number is smaller: "))
    else:
        print("Sorry, you lost.")
else:
    print("Congratsulations, the secret number was 7. You won! ")
    
