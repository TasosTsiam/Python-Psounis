hours = 2
minutes = 35
seconds = 20
t_seconds = (hours * 3600) + (minutes * 60) + seconds
print(t_seconds)

hours2 = 2
minutes2 = 35
seconds2 = 20
t_seconds2 = seconds2
t_seconds2 += minutes2 * 60
t_seconds2 += hours2 * 3600
print(t_seconds2)
