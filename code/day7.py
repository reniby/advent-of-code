import re

#Count card frequencies and sort hands into array by rank
#hands = [high card hand, pair, two pair, 3 kind, full house, 4 kind, 5 kind]
def parseInput(part):
    hands = [[] for i in range(7)]
    bids = {}
    with open('inputs/day7.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '').split(' ')
            bids[line[0]] = line[1]

            currHand = { 'A': 0 }
            currCount = [0] * 6

            if part == 1:
                for i in line[0]:
                    currHand[i] = currHand.get(i,0)+1
                for i in currHand:
                    currCount[currHand[i]] += 1
            elif part == 2:
                jokers = 0
                for i in line[0]:
                    if i != 'J':
                        currHand[i] = currHand.get(i,0)+1
                    else:
                        jokers += 1
                maxCard = max(currHand, key=lambda x: currHand[x])
                currHand[maxCard] += jokers
                for i in currHand:
                    if i != 'J':
                        currCount[currHand[i]] += 1
    
            if currCount[5] == 1: hands[6].append(line[0])
            elif currCount[4] == 1: hands[5].append(line[0])
            elif currCount[3] == 1 and currCount[2] == 1: hands[4].append(line[0])
            elif currCount[3] == 1: hands[3].append(line[0])
            elif currCount[2] == 2: hands[2].append(line[0])
            elif currCount[2] == 1: hands[1].append(line[0])
            else: hands[0].append(line[0])
    return hands, bids

#Recursive function to sort hands by rank
#First sorted based on rank, then on value of card 1, then card 2, etc.
def splitHands(hands, idx, part):
    newSplit = [[] for i in range(13)]

    if part == 1:
        for i in hands:
            if i[idx] == 'A': newSplit[12].append(i)
            elif i[idx] == 'K': newSplit[11].append(i)
            elif i[idx] == 'Q': newSplit[10].append(i)
            elif i[idx] == 'J': newSplit[9].append(i)
            elif i[idx] == 'T': newSplit[8].append(i)
            else: newSplit[int(i[idx])-2].append(i)
    elif part == 2:
        for i in hands:
            if i[idx] == 'A': newSplit[12].append(i)
            elif i[idx] == 'K': newSplit[11].append(i)
            elif i[idx] == 'Q': newSplit[10].append(i)
            elif i[idx] == 'J': newSplit[0].append(i)
            elif i[idx] == 'T': newSplit[9].append(i)
            else: newSplit[int(i[idx])-1].append(i)
    
    for i in range(13):
        if len(newSplit[i]) > 1:
            newSplit[i] = splitHands(newSplit[i], idx+1, part)    
    return newSplit

#Multiply bids by rank and return result
def calculateResult(hands, bids, part):
    rank = 1
    result = 0
    for i in hands:
        if len(i) == 1:
            result += rank * int(bids[i[0]])
            rank += 1
        else:
            flattened = re.findall(r'\w{5}', str(splitHands(i, 0, part)))
            for f in flattened:
                result += rank * int(bids[f])
                rank += 1
    return result

if __name__ == "__main__":
    for i in range(1,3):
        hands, bids = parseInput(i)
        result = calculateResult(hands, bids, i)
        print('Part ' + str(i) + ':', result)