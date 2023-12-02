#Part 1
with open('inputs/day1.txt', 'r') as file:
    sum = 0
    for line in file:
        nums = ''
        for char in line:
            if char in '0123456789': nums += char
        sum += int(nums[0] + nums[len(nums)-1])
    print('Day 1: ', sum)

#Part 2
hm = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('inputs/day1.txt', 'r') as file:
    sum = 0
    for line in file:
        currStr = ''
        nums = ''
        for char in range(0, len(line)):
            currStr += line[char]
            if line[char] in '0123456789':
                nums += line[char]
                currStr = ''
            else:
                for i in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']:
                    if i in currStr:
                        nums += hm[i]
                        currStr = currStr[len(currStr)-len(i):]
        sum += int(nums[0] + nums[len(nums)-1])
    print('Day 2: ', sum)