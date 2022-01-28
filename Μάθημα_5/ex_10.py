#Τρόπος δικός μου.
bfriends = ["Stefanos", "Panagiotis", "Giorgos"]
invited = ["M", "Panagiotis", "G", "S", "T", "M", "Stefanos", "L", "St", "Giorgos"]
bfriends_invited = 0
bfriends_inv_req = 2
while True:
    if bfriends[0] in invited:
        bfriends_invited += 1
    if bfriends[1] in invited:
        bfriends_invited += 1
    if bfriends[2] in invited:
        bfriends_invited += 1
    if bfriends_invited >= bfriends_inv_req:
        print("Έρχομαι ρε μάνμου!")
    else:
        print("Δύσκολα, θα μείνω μέσα.")
    break

#Τρόπος του Καθηγητή.
bfriends = ["Stefanos", "Panagiotis", "Giorgos"]
invited = ["M", "Panagiotis", "G", "S", "T", "M", "Stefanos", "L", "St", "Giorgos"]
bfriends_invited = 0
for friend in bfriends:
    if friend in invited:
        bfriends_invited += 1
if bfriends_invited < 2:
    print("Δύσκολα, θα μείνω μέσα.")
else:
    print("Έρχομαι ρε μάνμου!")
