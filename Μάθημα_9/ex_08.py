poem = """ There's a bluebird in my heart that
wants to get out
but I'm too tough for him,
I say,
stay down, do you want to mess me up?
you want to screw up the works?
you want to blow my book sales in Europe?
"""
print(poem)
print("")
poem_list = poem.splitlines()


while True:
    string = input("Give a word, taken from the quote: ")

    if string.isalpha():
        word = string.lower()
        print(f"Word entered: {string}")
        for pos in range(len(poem_list)):
            if poem_list[pos].find(word) != -1:
                print(f"Line {pos+1}: {poem_list[pos].replace(word, word.upper())}")
        break
    else:
        print("LETTERS mf please! ")
