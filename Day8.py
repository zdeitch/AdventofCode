points = []
with open("Day8File.txt") as file:
    for line in file:
        x, y, z = map(int, line.strip().split(','))
        points.append((x, y, z))

distances = []
for point_index1 in range(len(points)):
    x1, y1, z1 = points[point_index1]
    for point_index2 in range(point_index1 + 1, len(points)):
        x2, y2, z2 = points[point_index2]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        distance = (dx*dx + dy*dy + dz*dz)**0.5
        distances.append((point_index1, point_index2, distance))

distances.sort(key=lambda entry: entry[2])

circuits = []
for i in range(len(points)):
    circuits.append([i])

attempt_count = 0
max_attempts = 1000

for entry in distances:
    if attempt_count == max_attempts:
        break

    point_index1 = entry[0]
    point_index2 = entry[1]

    circuit_index1 = -1
    circuit_index2 = -1
    for index in range(len(circuits)):
        circuit = circuits[index]
        for p in circuit:
            if p == point_index1:
                circuit_index1 = index
            if p == point_index2:
                circuit_index2 = index
        if circuit_index1 >= 0 and circuit_index2 >= 0:
            break

    if circuit_index1 != circuit_index2:
        circuits[circuit_index1] += circuits[circuit_index2]
        del circuits[circuit_index2]

    attempt_count += 1

circuit_sizes = []
for circuit in circuits:
    circuit_sizes.append(len(circuit))
circuit_sizes.sort(reverse=True)

print("PART 1 SOLUTION:", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])

circuits = []
for i in range(len(points)):
    circuits.append([i])

last_connection = []

for entry in distances:
    point_index1 = entry[0]
    point_index2 = entry[1]

    circuit_index1 = -1
    circuit_index2 = -1
    for index in range(len(circuits)):
        circuit = circuits[index]
        for p in circuit:
            if p == point_index1:
                circuit_index1 = index
            if p == point_index2:
                circuit_index2 = index
        if circuit_index1 >= 0 and circuit_index2 >= 0:
            break

    if circuit_index1 != circuit_index2:
        last_connection = [point_index1, point_index2]
        circuits[circuit_index1] += circuits[circuit_index2]
        del circuits[circuit_index2]

    if len(circuits) == 1:
        break

x1 = points[last_connection[0]][0]
x2 = points[last_connection[1]][0]
product_x = x1 * x2
print("PART 2 SOLUTION: ",product_x)
