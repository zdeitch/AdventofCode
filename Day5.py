with open("Day5File.txt", 'r') as file:
    all_lines = file.readlines()

ranges = []
ids = []
reading_ranges = True

for line in all_lines:
    stripped_line = line.strip()

    if stripped_line == '':
        reading_ranges = False
        continue

    if reading_ranges:
        ranges.append(stripped_line)
    elif stripped_line != '':
        ids.append(stripped_line)

fresh_count = 0
for id_str in ids:
    id = int(id_str)
    
    for range_str in ranges:
        bounds = range_str.split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1]) 
                

        if id >= lower_bound and id <= upper_bound:
            fresh_count += 1
            break

print("PART 1 SOLUTION: ",fresh_count)


###### PART 2

amount = 0
future_ranges = ranges
skip_indices = []
amount = 0
future_ranges = ranges
skip_indices = []
for i in range(len(ranges)):
    if i in skip_indices:
        continue
    #print("Range: ",ranges[i])
    future_ranges = ranges[i+1:]
    #print("Futures: ",future_ranges)
    bounds = ranges[i].split('-')
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
     #we are gonna split into cases to determine overlap for all future ranges, and keep trimming down the current range
    for j in range(len(future_ranges)):
        if j+i+1 in skip_indices:
            continue
        lb = int(future_ranges[j].split('-')[0]) #lower and upper bounds of the future range
        ub = int(future_ranges[j].split('-')[1])

        #5 CASES OF OVERLAP
        if lb >= lower_bound and ub <= upper_bound:
            skip_indices.append(i+j+1)
            case_true = 5
            continue

        if lower_bound >= lb and upper_bound <= ub:
            case_true = 1
            lower_bound = None
            break

        if lb <= lower_bound <= ub < upper_bound:
            lower_bound = ub + 1
            case_true = 2
            continue

        if lower_bound < lb <= upper_bound <= ub:
            upper_bound = lb - 1
            case_true = 3
            continue

        if lower_bound > ub or lb > upper_bound:
            case_true = 4
            continue

    #still add the amount
    if lower_bound is not None and lower_bound <= upper_bound:
        amount += upper_bound - lower_bound + 1

print("PART 2 SOLUTION: ",amount)

    

