#Part 1 and 2

with open('inputs/day9.txt', 'r') as file:
    part1 = []
    part2 = []
    for line in file:
        prev = [int(i) for i in line.split(' ')]

        #save first and last value to add and subtract from later
        adds = [prev[-1]]
        subs = [prev[0]]

        all_zeros = False
        while (not all_zeros):
            all_zeros = True
            curr = []

            #calculate differences between consecutive numbers
            for i in range(1, len(prev)):
                curr.append(prev[i] - prev[i-1])
                if curr[i-1] != 0:
                    all_zeros = False

            prev = curr
            adds.append(prev[-1])
            subs.append(prev[0])

        #propogate adds and subtracts back to original values
        for i in range(len(adds)-2, -1, -1):
            adds[i] += adds[i+1]
            subs[i] -= subs[i+1]
        
        part1.append(adds[0])
        part2.append(subs[0])
    
    print('Part 1:', sum(part1))
    print('Part 2:', sum(part2))