file = open("7/input.txt", "r")
lines = file.readlines()
manifold_diagram = []
for line in lines:
    manifold_diagram.append(line.strip())
    
R_max = len(manifold_diagram)
C_max = len(manifold_diagram[0])

start_row = -1
start_col = -1
for r in range(R_max):
    if 'S' in manifold_diagram[r]:
        start_row = r
        start_col = manifold_diagram[r].index('S')
        break

timelines = [[0] * C_max for _ in range(R_max)]

timelines[start_row][start_col] = 1

for r in range(start_row, R_max - 1):
    
    current_row_config = manifold_diagram[r]
    
    for c in range(C_max):
        
        current_timeline_count = timelines[r][c]
        if current_timeline_count == 0:
            continue
            
        cell = current_row_config[c]
        
        if cell == '.' or cell == 'S':
            timelines[r + 1][c] += current_timeline_count
            
        elif cell == '^':
            if c - 1 >= 0:
                timelines[r + 1][c - 1] += current_timeline_count

            if c + 1 < C_max:
                timelines[r + 1][c + 1] += current_timeline_count

total_timelines = sum(timelines[R_max - 1])

print(f"Total active timelines: {total_timelines}")