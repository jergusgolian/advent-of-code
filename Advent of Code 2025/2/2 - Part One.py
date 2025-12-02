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
        if len(check) % 2 == 0:
            half = len(check) // 2
            first_half = check[:half]
            second_half = check[half:]
            if first_half == second_half:
                j_list.append(n)
    print(j)
    print(j_list)
    print()
    for m in j_list:
        invalid_sum += m

print(f"Adding up all the invalid IDs in this example produces {invalid_sum}")