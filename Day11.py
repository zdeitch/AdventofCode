

## i wanna do a depth first search in a graph (in the form of dictionary of these things
#edges represent connections
#we add to a count each time we hit "out" starting from "you"

graph = dict()
# the inputs are gonna be the starting nodes for each line. 
with open("Day11File.txt", "r") as file:
    for line in file:
        line = line.strip()
        
        split_line = line.split(':')
        
        in_node = split_line[0].strip()
        
        out_nodes = split_line[1].strip().split(' ')
        adjacent_list = []
        for out_node in out_nodes:
            adjacent_list.append(out_node)
        graph[in_node] = adjacent_list



#node is represented by a string.
def count_all_paths(starting_node, ending_node, visited):
    
    if starting_node == ending_node:
        return 1
    visited.append(starting_node)
    path_count = 0
    for adjacent_node in graph[starting_node]:
        if adjacent_node not in visited:
            path_count += count_all_paths(adjacent_node,ending_node, visited)
    visited.remove(starting_node)
    return path_count
            
visited = []
print("PART 1 SOLUTION: ", count_all_paths('you', 'out', visited))

## PART 2


path_count_dict = {}

def count_all_paths2(starting_node, ending_node, visited, dac_found,fft_found):
    key = (starting_node, dac_found, fft_found)
    if starting_node == 'dac':
        dac_found = True
    if starting_node == 'fft':
        fft_found = True
    if starting_node == ending_node:
        if dac_found and fft_found:
            return 1
        else:
            return 0
    if key in path_count_dict.keys():
        return path_count_dict[key]
    visited.append(starting_node)
    path_count = 0
    for adjacent_node in graph[starting_node]:
        if adjacent_node not in visited:
            path_count += count_all_paths2(adjacent_node,ending_node,visited, dac_found,fft_found)

    key = (starting_node, dac_found, fft_found)
    path_count_dict[key] = path_count
    visited.remove(starting_node)
    return path_count


visited = []
print("PART 2 SOLUTION: ", count_all_paths2('svr', 'out', visited, False, False))
    



        
        
        
        
