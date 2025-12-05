file = open("5/input.txt", "r")
instructions = file.readlines()

ids = []
ing = []
good = 0
part = False

for line in instructions:
    line = line.strip()
    if line == "":
        part = True
    else:
        if part == False:
            first = ""
            second = ""
            id_part = False
            for char in line:
                if char == "-":
                    id_part = True
                else:
                    if id_part == False:
                        first += str(char)
                    else:
                        second += str(char)
            ids.append([first, second])
        else:
            ing.append(line)
    
for id in ing:
    for rng in ids:
        if int(rng[0]) <= int(id) <= int(rng[1]):
            good +=1
            break


print(f"Count of good ingredients is: {good}")