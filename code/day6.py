#Part 1

time = []
distance = []
with open('inputs/day6.txt', 'r') as file:
    currMap = time
    for line in file:
        line = line.replace('\n', '').split(' ')
        for l in line:
            if l != '' and ':' not in l:
                currMap.append(l)
        currMap = distance

result = 1
for t in range(len(time)):
    currTime = int(time[t])
    currDistance = int(distance[t])
    temp = 0
    for r in range(currTime):
        if r * (currTime-r) > currDistance:
            temp = r
            break
    for r in range(currTime-1, -1, -1):
        if r * (currTime-r) > currDistance:
            temp = r - temp + 1
            break
    result *= temp

print('Part 1:', result)




#Part 2
vals = []
with open('inputs/day6.txt', 'r') as file:
    currVal = time
    for line in file:
        line = line.replace('\n', '').replace(' ','').split(':')
        vals.append(line[1])

print(vals)
currTime = int(vals[0])
currDistance = int(vals[1])
result = 0
for r in range(currTime):
    if r * (currTime-r) > currDistance:
        result = r
        break
for r in range(currTime-1, -1, -1):
    if r * (currTime-r) > currDistance:
        result = r - result + 1
        break

print('Part 2:', result)