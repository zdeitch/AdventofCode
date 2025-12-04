#Problem 3 part 1

def findmax(line, last_char):
    max_val = 0     
    max_index = 0
    
    end = len(line) if last_char else len(line) - 1
    
    for i in range(end):   #all but last number for first one
        current_character = int(line[i])
        
        if current_character > max_val: 
            max_val = current_character
            max_index = i

    return max_val, max_index


def find_joltage_sum(filename):
    with open(filename, 'r') as file:
        sum = 0
        for line in file:
            line=line.strip()
            #First number
            max1, max_index1 = findmax(line, False) #int, int
            
            #second number
            sub_line = line[max_index1+1:]
            max2, max_index2 = findmax(sub_line, True) #int, int
            joltage = int(line[max_index1]+sub_line[max_index2])
            print("LINE: ",line)
            print("MAXIND1: ", max_index1)
            print("SUB_LINE: ",sub_line)
            print("MAXIND2: ", max_index2)
            print(line[max_index1]+sub_line[max_index2])
            print('\n')
        
            sum += joltage
    return sum


#print("PART 1 SOLUTION: "find_joltage_sum('Day3File.txt'))

#### Part 2 

def findmax_2(line, spaces_to_leave):
    max_val = 0     
    max_index = 0
    
    end = len(line) - spaces_to_leave
    
    for i in range(end):   #all but last number for first one
        current_character = int(line[i])
        
        if current_character > max_val: 
            max_val = current_character
            max_index = i

    return max_val, max_index


def find_joltage_sum_2(filename):
    with open(filename, 'r') as file:
        sum = 0
        for line in file:
            line=line.strip()
            max_indices = []
            newline=line
            orig_max_index = 0
            
            for iteration in range(12):
                #print(line)
                max, max_index = findmax_2(newline, 11-iteration) #int, int
                orig_max_index = orig_max_index + max_index + 1
                #print(newline)
                #print("MAX "+str(iteration)+" "+ str(max))
                #print("ORIG_MAX_INDX"+str(iteration)+" "+ str(orig_max_index))
                max_indices.append(orig_max_index-1)
                newline = newline[max_index+1:]
                
                    
            #print(max_indices)
            joltage_string = '0'
            for index in max_indices:
                joltage_string += str(line[index])
            #print(joltage_string)
            #print("========================")
            joltage = int(joltage_string)
            sum += joltage
            
    return sum

print("PART 2 SOLUTION: ",find_joltage_sum_2('Day3File.txt'))

