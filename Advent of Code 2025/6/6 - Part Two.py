file = open("/storage/emulated/0/PyDroid/6/input.txt", "r")
lines = file.readlines()
clean_lines = [ ]

for i in range(len(lines) - 1):
    clean_lines.append(lines[i].rstrip("\n"))

operators = [ ]
for char in lines[-1]:
    if char != " " and char != "\n":
        operators.append(char)

lines = clean_lines

all_numbers = [list(row) for row in zip(*lines)]

all_numbers = all_numbers[::-1]
operators = operators[::-1]

formated_numbers = [ ]

for number in all_numbers:
    if number.count(' ') == len(number):
        formated_numbers.append(' ')
    else:
        n = ''.join(number).strip()
        formated_numbers.append(n)

column = [ ]
grouped_numbers = [ ]
final_sum = 0

for number in formated_numbers:
    if number != ' ':
        column.append(number)
    else:
        grouped_numbers.append(column)
        column = [ ]

if column != []:
    grouped_numbers.append(column)

for i in range(len(grouped_numbers)):
    operant = operators[i]
    group = grouped_numbers[i]

    if operant == '*':
        total = 1
    else:
        total = 0

    for number in group:
        if operant == '*':
            total *= int(number)
        else:
            total += int(number)

    final_sum += total

print()
print(f"The grand total is {final_sum}")
