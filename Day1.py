

# FOR PART 1:

number = 50

file = open('Day1File.txt', 'r')
line = file.readline().strip()
zero_count = 0

while line != '':
    if line[0] == 'L':
        number = (number - int(line[1:]))%100

    elif line[0] == 'R':
        number = (number + int(line[1:]))%100

    if number == 0:
        zero_count += 1
        
    line = file.readline().strip()


print("PART ONE: ", zero_count)

# PART 2
number = 50

with open('Day1File.txt', 'r') as file:
    zero_count_II = 0

    for line in file:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        amount = int(line[1:])

        if direction == 'R':
            zero_count_II += (number + amount) // 100
            number = (number + amount) % 100

        else:  
            if number == 0:
                zero_count_II += amount // 100
            else:
                if amount >= number:
                    zero_count_II += (amount - number) // 100 + 1
            number = (number - amount) % 100

print("PART TWO:", zero_count_II)


