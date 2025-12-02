file = open("2/input.txt", "r")
instructions = file.readline()
parts = instructions.split(",")
instructions = [ ]

invalid_sum = 0

for i in range(len(parts)):
    part = parts[i]
    if part[0] == " ":
        instructions.append(part[1:])
    else:
        instructions.append(parts[i])
        
for j in instructions:    
    id_parts = str(j).split("-")
    
    first = int(id_parts[0])
    second = int(id_parts[1])
    
    j_list = [ ]
    
    for n in range(first, second+1):
        check = str(n)
        lenght = len(check)
        for x in range(1, lenght // 2 +1):
            if lenght % x == 0:
                block = check[:x]
                repeat = lenght // x
                if block*repeat == check and repeat >= 2:
                    j_list.append(n)
                    break
    print(j)
    print(j_list)
    print()
    for m in j_list:
        invalid_sum += m

print(f"Adding up all the invalid IDs in this example produces {invalid_sum}")