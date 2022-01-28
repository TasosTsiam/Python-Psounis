#Επίτηδες πρόσθεσα κι άλλα παραδείγματα, για να συνειδητοποιήσω την αναγκαιότητα
#του να μην βάλω .pop(1) στην άσκηση επειδή η λίστα είχε εκείνη την ώρα μόνο 2 στοιχεία,
#μα να βάλω .pop() εφόσον αυτό που με ενδιέφερε, είναι κάθε φορά, να τσεκάρει το τελευταίο στοιχείο,
#ανεξάρτητα απ' το πόσα στοιχεία έχει η λίστα.'
documents = []
documents.append("Bob")
documents.append("John")
print(documents)
document_check = documents.pop()
print(document_check + "'s document file has been checked.")
documents.append("Pat")
documents.append("Phoebe")
documents.append("Joey")
documents.append("Ross")
documents.append("Rachel")
documents.append("Chandler")
documents.append("Monica")
print(documents)
document_check = documents.pop()
print(document_check + "'s document file has been checked.")
document_check = documents.pop()
print(document_check + "'s document file has been checked.")
document_check = documents.pop()
print(document_check + "'s document file has been checked.")
document_check = documents.pop()
print(document_check + "'s document file has been checked.")
document_check = documents.pop()
print(document_check + "'s document file has been checked.")
