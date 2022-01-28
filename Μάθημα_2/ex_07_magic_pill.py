name = input("Type your Name: ")
surname = input("Type your Surname: ")
age = int(input("Type your Age: "))
magic_pill = 10
age -= magic_pill
message = "Hello " + name + " " + surname
message_age = ". You are " + str(age) + " years old!"
print(message + message_age)
