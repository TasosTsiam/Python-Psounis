age = int(input("Enter your Age: "))
if age < 18:
    print("Ανήλικος")
elif age >= 18 and age <= 65:
    print("Ενήλικος")
else:
    print("Συνταξιούχος")
