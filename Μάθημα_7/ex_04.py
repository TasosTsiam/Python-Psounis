#Χωρισμός σε Ομάδες:
# Η δασκάλα μιας τάξης θέλει να κατασκευάσει ένα πρόγραμμα το οποίο:
# 1) Δεδομένων των Ν(έστω Ν άρτιος) μαθητών της
# 2) Θα τους χωρίζει σε Ν/2 ομάδες των μαθητών, με τυχαίο τρόπο,
#    ώστε να τους αναθέσει μια ομαδική εργασία.
# Βοηθήστε την δασκάλα ώστε να κάνει δύο χωρισμούς σε τυχαίες ομάδες των 2,
# έναν για το μάθημα των μαθηματικών και έναν για το μάθημα της γεωγραφίας.

from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 10
pupils = set()
for number in range(N):
    pupils.add("student " + str(number))


list_pupils = list(pupils)
math_teams = set()
for i in range(N // 2):
    pos1 = randrange(0, len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    math_teams.add(team)
print("Math teams: " + str(math_teams))

list_pupils = list(pupils)
geography_teams = set()
for i in range(N // 2):
    pos1 = randrange(0, len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    geography_teams.add(team)
print("")
print("Geography teams: " + str(geography_teams))
