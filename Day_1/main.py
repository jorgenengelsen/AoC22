f = open("input.txt", "r")
lines = f.readlines()

gnomes = []
gnome = []
for line in lines:
    if line == "\n":
        gnomes.append(gnome)
        gnome = []
        continue
    gnome.append(int(line.strip()))

max_calories = 0
gnome_index = 0
for i, gnome in enumerate(gnomes):
    if sum(gnome) > max_calories:
        max_calories = sum(gnome)
        gnome_index = i

print(gnome_index)
print(max_calories)
    

calories = [sum(gnome) for gnome in gnomes]
calories.sort()

print(calories[-3:])
print(sum(calories[-3:]))
