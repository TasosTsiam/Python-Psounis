my_quote_string = "I don't hate them...I just feel better when they're not around."
print("""Please try to type the word specifically the way it's written.
Also, only one word is required.
Also, no damn spaces in between!
If you want to quit this program, just type 'quit'.""")
print("")
print("Quote: \n" + my_quote_string)
print("")


while True:
    user_input = input("Enter a word from the quote: ")
    if user_input == "quit":
        quit()
    elif user_input not in my_quote_string or " " in user_input:
        print("")
        print("The damn suggestions. See them? That's what you gonn' do. ")
        print("")
        continue
    else:
        pos = my_quote_string.find(user_input)
        if my_quote_string.startswith(user_input, pos):
            my_quote_string = my_quote_string.replace(user_input, user_input.upper(), 1)
            print(my_quote_string)

        #Δική μου πινελιά, εξέλιξη της άσκησης, ώστε να τερματίζει όταν όλα τα γράμματα
        #γίνουν κεφαλαία στο ρητό.
        if my_quote_string == my_quote_string.upper():
            print("All laters are now capitalized. See ya.")
            quit()
