# I think we can use an integer program to solve (i learned about this in math 331 Operations Research)
# it uses a modified algorithm based on the simplex method to solve linear programs. 
#Just need to formulate the objective function (total number of buttos pressed, to be minimized) and the constraints, namely the limits on number of button pressed, and non-negativity.
import re
from itertools import combinations
import pulp

def row_reduce_gf2(matrix, rhs_vector):
    matrix_copy = [row[:] for row in matrix]
    rhs_copy = rhs_vector[:]
    num_rows = len(matrix_copy)
    num_cols = len(matrix_copy[0])
    pivot_columns = []
    current_row = 0
    for col in range(num_cols):
        pivot_row = None
        for r in range(current_row, num_rows):
            if matrix_copy[r][col] == 1:
                pivot_row = r
                break
        if pivot_row is None:
            continue
        matrix_copy[current_row], matrix_copy[pivot_row] = matrix_copy[pivot_row], matrix_copy[current_row]
        rhs_copy[current_row], rhs_copy[pivot_row] = rhs_copy[pivot_row], rhs_copy[current_row]
        pivot_columns.append(col)
        for r in range(num_rows):
            if r != current_row and matrix_copy[r][col] == 1:
                for c in range(col, num_cols):
                    matrix_copy[r][c] ^= matrix_copy[current_row][c]
                rhs_copy[r] ^= rhs_copy[current_row]
        current_row += 1
    free_columns = [c for c in range(num_cols) if c not in pivot_columns]
    return matrix_copy, rhs_copy, pivot_columns, free_columns

def back_substitute_gf2(reduced_matrix, reduced_rhs, pivot_columns, free_assignments):
    num_rows = len(reduced_matrix)
    num_cols = len(reduced_matrix[0])
    solution = [0]*num_cols
    for col in free_assignments:
        solution[col] = free_assignments[col]
    pivot_row_index = 0
    for col in pivot_columns:
        rhs_value = reduced_rhs[pivot_row_index]
        dot = 0
        for j in range(col+1, num_cols):
            if reduced_matrix[pivot_row_index][j] == 1:
                dot ^= solution[j]
        solution[col] = rhs_value ^ dot
        pivot_row_index += 1
    return solution

def compute_minimum_presses(toggle_matrix, target_vector):
    reduced_matrix, reduced_rhs, pivot_columns, free_columns = row_reduce_gf2(toggle_matrix, target_vector)
    fewest_presses = 1000000
    for k in range(len(free_columns)+1):
        for combo in combinations(free_columns, k):
            free_assignment = {c:0 for c in free_columns}
            for c in combo:
                free_assignment[c] = 1
            candidate = back_substitute_gf2(reduced_matrix, reduced_rhs, pivot_columns, free_assignment)
            presses = sum(candidate)
            if presses < fewest_presses:
                fewest_presses = presses
    return fewest_presses

def parse_machine_line_part1(line):
    light_pattern = re.search(r"\[(.*?)\]", line).group(1)
    target_vector = [1 if ch=="#" else 0 for ch in light_pattern]
    button_groups = re.findall(r"\((.*?)\)", line)
    button_lists = []
    for group in button_groups:
        if group.strip()=="":
            button_lists.append([])
        else:
            button_lists.append([int(x) for x in group.split(",")])
    num_lights = len(target_vector)
    num_buttons = len(button_lists)
    toggle_matrix = [[0]*num_buttons for _ in range(num_lights)]
    for j in range(num_buttons):
        for light in button_lists[j]:
            toggle_matrix[light][j] = 1
    return toggle_matrix, target_vector

def solve_file_part1(file_path):
    total_presses = 0
    file_handle = open(file_path)
    for line in file_handle:
        line = line.strip()
        if line=="":
            continue
        toggle_matrix, target_vector = parse_machine_line_part1(line)
        presses = compute_minimum_presses(toggle_matrix, target_vector)
        total_presses += presses
    file_handle.close()
    return total_presses

def parse_machine_line_part2(line):
    button_groups = re.findall(r"\((.*?)\)", line)
    buttons = []
    for group in button_groups:
        if group.strip()=="":
            buttons.append([])
        else:
            buttons.append([int(x) for x in group.split(",")])
    targets_match = re.search(r"\{(.*?)\}", line)
    targets = [int(x) for x in targets_match.group(1).split(",")]
    return buttons, targets

def solve_machine_part2(buttons, targets):
    num_buttons = len(buttons)
    num_targets = len(targets)
    problem = pulp.LpProblem("ButtonPressMinimization", pulp.LpMinimize)
    press_vars = [pulp.LpVariable(f"press_{j}", lowBound=0, cat="Integer") for j in range(num_buttons)]
    for target_index in range(num_targets):
        problem += pulp.lpSum(press_vars[j] for j in range(num_buttons) if target_index in buttons[j]) == targets[target_index]
    problem += pulp.lpSum(press_vars)
    problem.solve()
    return int(sum(var.value() for var in press_vars))

total_part1 = solve_file_part1("Day10File.txt")
print("PART 1 SOLUTION:", total_part1)

## PART 2
#we gonna do a similar approach, but instead, we can just make it so that instead,
#we can formulate in terms of actions rather than binary, where presses are full integers
total_part2 = 0
file_handle = open("Day10File.txt")
for line in file_handle:
    line = line.strip()
    if line=="":
        continue
    buttons, targets = parse_machine_line_part2(line)
    presses = solve_machine_part2(buttons, targets)
    total_part2 += presses
file_handle.close()
print("PART 2 SOLUTION:", total_part2)
