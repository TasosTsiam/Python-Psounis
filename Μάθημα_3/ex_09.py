hours = int(input("Enter Hours: "))
minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter seconds: "))
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
hms = str(hours) + ":" + str(minutes) + ":" + str(seconds)
print(hms)
