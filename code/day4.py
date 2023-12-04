#Part 1 and 2

cards = {}
with open('inputs/day4.txt', 'r') as file:
    part1 = 0
    for line in file:
        #Parse input line
        lineResult = 0
        line = line.replace('   ', ' ').replace('  ', ' ').replace('\n', '').split(' | ')
        l = line[0].split(' ')
        r = line[1].split(' ')
        numbers = r

        #Part 1
        for i in range(2, len(l)):
            if l[i] in numbers:
                if lineResult == 0:
                    lineResult = 1
                else:
                    lineResult *= 2
        part1 += lineResult
        
        #Part 2
        wins = 0
        currIdx = int(l[1][:len(l[1])-1])
        cards[currIdx] = cards.get(currIdx, 0) + 1
        for i in range(2, len(l)):
            if l[i] in numbers:
                wins += 1
        for i in range(currIdx+1, currIdx+wins+1):
            cards[i] = cards.get(i, 0) + cards[currIdx]
        part2 = 0
        for i in cards:
            part2 += cards[i]


    print('Part 1: ', part1)
    print('Part 2: ', part2)
