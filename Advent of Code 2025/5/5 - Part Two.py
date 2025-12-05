file = open("5/input.txt", "r")
instructions = file.readlines()

ranges = []
found_blank_line = False

for line in instructions:
    line = line.strip()
    if line == "":
        found_blank_line = True
        continue
    
    if not found_blank_line:
        start_str, end_str = line.split('-')
        ranges.append((int(start_str), int(end_str)))

ranges.sort()

consolidated_ranges = []
if ranges:
    current_start, current_end = ranges[0]

    for next_start, next_end in ranges[1:]:
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            consolidated_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end
            
    consolidated_ranges.append((current_start, current_end))


total_fresh_ids = 0
for start, end in consolidated_ranges:
    total_fresh_ids += (end - start + 1)

print(f"Count of fresh ingredient IDs is: {total_fresh_ids}")