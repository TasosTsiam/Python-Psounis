paragraph = "Epic Games' Fortnite is about to go from massive to... Even bigger than massive. The Chapter 2 Finale is on the way and we're about to enter uncharted waters again with a new Chapter of Fortnite content that promises to continue to break boundaries and impress. We don't think the onslaught of collaborative content is going anywhere, but there's a lot more to come from Fortnite - which is as much a battle royale game as it is a sandbox game. Here's everything you need to know about Fortnite Chapter 3 - well, what we know so far."

print(paragraph)
paragraph = list(paragraph)
print(paragraph)

#I must create a dictionary to count how many times each letter of "paragraph" is being used,
#whereas keys will be the letters, and values will be the amount of times.
dict_paragraph = {}
for i in paragraph:
    if i not in dict_paragraph:
        dict_paragraph[i] = 1
    else:
        dict_paragraph[i] += 1
print(dict_paragraph)

biggest_so_far = 0
for value in dict_paragraph.values():
    if biggest_so_far <= value:
        biggest_so_far = value
print(biggest_so_far)
for key in dict_paragraph.keys():
    if dict_paragraph[key] == biggest_so_far:
        print("' " + str(key) + " '" + " is the most used character with " + str(biggest_so_far) + " times used.")
