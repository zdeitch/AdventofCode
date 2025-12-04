


with open("Day4File.txt", 'r') as file:
# 2d list
    grid = []
    for line in file:
        row = []
        for ch in line:
            if ch != '\n':
                row.append(ch)
        grid.append(row)
            
            
#each thing is grid[row][column]

#DIMENSIONS
#print(len(grid)) #Vertical
#print(len(grid[1])) #Horiz.


def count_adjacent(grid, row, col): #count number of toilet paper
    c = 0
    if row > 0 and col < len(grid[row-1]) and grid[row-1][col] == '@': c += 1
    if row < len(grid)-1 and col < len(grid[row+1]) and grid[row+1][col] == '@': c += 1
    if col > 0 and grid[row][col-1] == '@': c += 1
    if col+1 < len(grid[row]) and grid[row][col+1] == '@': c += 1
    if row > 0 and col > 0 and col-1 < len(grid[row-1]) and grid[row-1][col-1] == '@': c += 1
    if row > 0 and col+1 < len(grid[row-1]) and grid[row-1][col+1] == '@': c += 1
    if row < len(grid)-1 and col > 0 and col-1 < len(grid[row+1]) and grid[row+1][col-1] == '@': c += 1
    if row < len(grid)-1 and col+1 < len(grid[row+1]) and grid[row+1][col+1] == '@': c += 1
    return c

        
    

def check_all(grid,num_adjacent):
    num_rows = len(grid)
    num_cols = len(grid[1])
    
    accessible_count = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '@' and count_adjacent(grid, row, col) < num_adjacent:
                accessible_count += 1
    return accessible_count

print("PART 1 SOLUTION: ",check_all(grid, 4))


##############################

#PART 2:

def check_all_and_remove(grid,num_adjacent):
    num_rows = len(grid)
    num_cols = len(grid[1])
    
    num_removed = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '@' and count_adjacent(grid, row, col) < num_adjacent:
                num_removed += 1

                grid[row][col] = '.' # remove the toilet paper
        
                
    return new_grid, num_removed

new_grid = grid
accessible_count = 0
while check_all(new_grid,4)!= 0:
    new_grid, num_removed = check_all_and_remove(new_grid, 4)
    accessible_count += num_removed

print("PART 2 SOLUTION: ", accessible_count)
    
    
    
    
    
    
