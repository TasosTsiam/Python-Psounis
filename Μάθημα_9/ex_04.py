my_quote_string = """
How the hell could a person enjoy being awakened at 6:30AM,
by an alarm clock, leap out of bed, dress, force-feed, shit, piss,
brush teeth and hair, and fight traffic to get to a place
where essentially yo made lots of money for somebody else
and were asked to be grateful for the opportunity to do so?"""


my_quote_string2 = my_quote_string.lower()
my_quote_list = list(my_quote_string2)
my_quote_list.sort()
my_quote_dict = {}
letters = "abcdefghijklmnopqrstuvwxyz"
list_letters = list(letters)

for char in my_quote_list:
    if char in list_letters:
        if char not in my_quote_dict:
            my_quote_dict[char] = 1
        else:
            my_quote_dict[char] += 1

for key, value in my_quote_dict.items():
    print(str(key) + ": " + str(value))
