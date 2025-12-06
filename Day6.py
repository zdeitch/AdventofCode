
with open("Day6File.txt", 'r') as file:
    all_lines = file.readlines()


#we gonna transpose it so each row of new array is a problem 
num_problems = len(all_lines[1].split())
prob_array = [[] for i in range(len(all_lines))] 

for i in range(len(all_lines)):
    nums_list = all_lines[i].split()     
    for j in range(min(len(nums_list), num_problems)):
        #print(nums_list[j])
        prob_array[i].append(nums_list[j])

rows = len(prob_array)
cols = min(len(row) for row in prob_array)

transposed = []
for c in range(cols):
    new_row = []
    for r in range(rows):
        new_row.append(prob_array[r][c])
    transposed.append(new_row)

prob_array = transposed

print(prob_array)

#Now we do the math


total = 0
for problem in prob_array:
    sign_index = len(problem)-1
    sign = problem[sign_index]

    if sign == '*':
        product = 1
        for i in range(sign_index):
            product = product * int(problem[i])
        total += product
    elif sign =='+':
        sum = 0
        for i in range(sign_index):
            sum += int(problem[i])
        total+= sum

print("PART 1 SOLUTION:",total)


### Part 2

with open("Day6File.txt", 'r') as file:
    all_lines = [line.rstrip('\n') for line in file]

max_len = max(len(line) for line in all_lines)
for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].ljust(max_len)

char_grid = [list(line) for line in all_lines]

cols = len(char_grid[0])
rows = len(char_grid)
transposed = []
for c in range(cols):
    column = []
    for r in range(rows):
        column.append(char_grid[r][c])
    transposed.append(column)

def split_numbers(columns):
    groups = []
    current = []
    for col in columns:
        if all(ch == ' ' for ch in col[:-1]):
            if current:
                groups.append(current)
                current = []
        else:
            current.append(col)
    if current:
        groups.append(current)
    return groups

def str_to_number(s):
    num = 0
    for ch in s:
        num = num * 10 + (ord(ch) - ord('0'))
    return num

total = 0
for problem_cols in reversed(split_numbers(transposed)):
    operator = problem_cols[0][-1]
    numbers = []

    for num_cols in problem_cols:
        digits = ''.join(ch for ch in num_cols[:-1] if ch != ' ')
        if digits:
            numbers.append(str_to_number(digits))

    if operator == '+':
        problem_sum = 0
        for n in numbers:
            problem_sum += n
        total += problem_sum
    elif operator == '*':
        product = 1
        for n in numbers:
            product *= n
        total += product
    else:
        print(f"Unknown operator {operator}")

print(total)

