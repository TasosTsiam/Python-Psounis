my_quote_string = "I guess the only time most people think about injustice is when it happens to them."


my_quote_list = list(my_quote_string)
my_quote_list.sort()
my_quote_dict = {}
for char in my_quote_list:
    if char not in my_quote_dict:
        my_quote_dict[char] = 1
    else:
        my_quote_dict[char] += 1

for key, value in my_quote_dict.items():
    print(str(key) + ": " + str(value))
