#Part 1 and 2

def day11(expansionRate):
    
    #store galaxy coordinates
    galaxies = []
    with open('inputs/day11.txt', 'r') as file:
        row = 0
        for line in file:
            col = 0
            for char in line:
                if char == '#':
                    galaxies.append([row, col])
                col += 1
            row += 1

    #adjust rows to account for expansion
    prev = -1
    add = 0
    for i in galaxies:
        if i[0] > prev + 1:
            add += expansionRate - 1
        i[0] += add
        prev = i[0] - add

    #adjust cols
    galaxies.sort(key = lambda x: x[1])
    prev = -1
    add = 0
    for i in galaxies:
        if i[1] > prev + 1:
            add += expansionRate - 1
        i[1] += add
        prev = i[1] - add

    #compute result
    result = 0
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            result += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return result

if __name__ == "__main__":
    print('Part 1:', day11(2))
    print('Part 2:', day11(1000000))
