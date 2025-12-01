text = open("1/input.txt", "r")
instructions = text.readlines()
current_number = 50
zeros = 0

print(f"  - The dial starts by pointing at {current_number}.")

for i in range(len(instructions)):
    line = instructions[i].strip()
    direction = line[0]
    number = int(line[1:])

    for j in range(number):
        if direction == 'R':
            current_number = (current_number + 1) % 100
        elif direction == 'L':
            current_number = (current_number - 1 + 100) % 100
        if current_number == 0:
            zeros += 1
    print(f"  - The dial is rotated {line} to point at {current_number}.")

print()
print(f"Final count of zeros is {zeros}")
print()