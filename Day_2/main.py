f = open("input.txt", "r")
lines = f.readlines()

gnome_play = []
me_play = []
for line in lines:
    gnome_play.append(line[0])
    me_play.append(line[-1])

score = 0
for me, gnome in zip(me_play, gnome_play):
    if me == "X":
        score += 1
        if gnome == "A":
            score += 3
        elif gnome == "C":
             score +=6
    if me == "Y":
        score += 2
        if gnome == "B":
            score += 3
        elif gnome == "A":
            score +=6
    else:
        score += 3
        if gnome == "C":
            score += 3
        elif gnome == "B":
            score += 6
print(score)