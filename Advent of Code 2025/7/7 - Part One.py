file = open("7/input.txt", "r")
lines = file.readlines()
manifold_diagram = []
for line in lines:
    manifold_diagram.append(line.strip())

start_row_index = 0
start_col = manifold_diagram[start_row_index].index('S')

active_beams = {start_col}

total_splits = 0

for row_index in range(start_row_index + 1, len(manifold_diagram)):
    
    current_row = manifold_diagram[row_index]
    new_active_beams = set()
    
    for col in active_beams:
        
        if 0 <= col < len(current_row):
            
            cell = current_row[col]
            
            if cell == '.':
                new_active_beams.add(col)
                
            elif cell == '^':
                if col - 1 >= 0:
                    new_active_beams.add(col - 1)
                    
                if col + 1 < len(current_row):
                    new_active_beams.add(col + 1)
                    
                total_splits += 1
                
    active_beams = new_active_beams
    
    if not active_beams:
        break

print(f"Total splits: {total_splits}")