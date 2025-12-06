file = open("6/input.txt", "r")
lines = file.readlines()

all_numbers = []

for line in range(len(lines)):
    line = lines[line].strip()
    columns = line.split()
    all_numbers.append(columns)

all_numbers = [list(row) for row in zip(*all_numbers)]
final_sum = 0

for line in all_numbers:
    operation = line.pop(-1)
    if operation == "+":
        total = 0
    else:
        total = 1
    for number in line:
        number = int(number)
        if operation == "+":
            total += number
        else:
            total *= number
    
    final_sum += total
    print(operation, line, "=", total)

print()
print(f"The grand total is {final_sum}")