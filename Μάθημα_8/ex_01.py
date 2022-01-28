dict = {"Ιταμός" : ["Προκλητικός", "Αυθάδης", "Αναιδής"],
        "Όνειδος" : ["Ντροπή", "Καταισχύνη"],
        "Πομφόλυγες" : ["Αερολογίες", "Ανοησίες"]}
print(dict)
dict["Φληναφήματα"] = ["Ανοησίες", "Σαχλαμάρες"]
print(dict)
print("")
print("Enter a new pair inside the dictionary.")
print("")
user_input1 = input("Insert a key: ")
user_input2 = input("Insert a value: ")
dict[user_input1] = user_input2
print(dict)
