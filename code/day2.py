#Part 1 and 2

numberAvailable = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('inputs/day2.txt', 'r') as file:
    part1 = 0
    part2 = 0

    for line in file:
        minimumNeeded = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        line = line.split(" ")
        id = int(line[1][:len(line[1])-1])
        possible = True
        
        for i in range(2, len(line), 2):
            color = line[i+1].replace(',', '').replace(';', '').replace('\n', '')
            numberUsed = int(line[i])
            possible = possible and numberUsed <= numberAvailable[color]
            minimumNeeded[color] = max(numberUsed, minimumNeeded[color])

        part1 += possible * id

        power = 1
        for i in minimumNeeded:
            power *= minimumNeeded[i]
        part2 += power

    print('Part 1: ', part1)
    print('Part 1: ', part2)



'''
#If easier to read, below they are separated

#Part 1
numberAvailable = {
    'red': 12,
    'green': 13,
    'blue': 14
}
with open('inputs/day2.txt', 'r') as file:
    result = 0

    for line in file:
        line = line.split(" ")
        id = int(line[1][:len(line[1])-1])
        possible = True

        for i in range(2, len(line), 2):
            color = line[i+1].replace(',', '').replace(';', '').replace('\n', '')
            numberUsed = int(line[i])
            possible = possible and numberUsed <= numberAvailable[color]

        result += possible * id

    print('Part 1: ', result)


#Part 2
with open('inputs/day2.txt', 'r') as file:
    result = 0
    
    for line in file:
        minimumNeeded = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        line = line.split(" ")
        id = int(line[1][:len(line[1])-1])
        
        for i in range(2, len(line), 2):
            color = line[i+1].replace(',', '').replace(';', '').replace('\n', '')
            numberUsed = int(line[i])
            minimumNeeded[color] = max(numberUsed, minimumNeeded[color])
        
        power = 1
        for i in minimumNeeded:
            power *= minimumNeeded[i]
        result += power

    print('Part 2: ', result)
'''