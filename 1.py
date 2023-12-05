import data_getter

data = data_getter.get_data(1).splitlines()

# data = ["two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen"]

total = 0

for line in data:
    new_value = 0
    for i in range(0, len(line)):
        if line[i].isnumeric():
            new_value += (int(line[i]) * 10)
            break
    for i in range((len(line) - 1), -1, -1):
        if line[i].isnumeric():
            new_value += int(line[i])
            break

    total += new_value
    
print(f'For part one, the total sum is {total}')

words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total = 0

for line in data:
    print(line)
    value = 0

    bingo = False
    for i in range(0, len(line)):
        if line[i].isnumeric():
            value += (int(line[i]) * 10)
            bingo = True
        elif i >= 2:
            substring = line[0:i+1]
            for word in words.keys():
                if word in substring:
                    bingo = True
                    value += words[word] * 10
                    break
        if bingo:
            break
    
    bingo = False
    for i in range(-1, -len(line)-1, -1):
        if line[i].isnumeric():
            bingo = True
            value += int(line[i])
            break
        elif i <= -3:
            substring = line[i:]
            for word in words.keys():
                if word in substring:
                    bingo = True
                    value += words[word]
                    break
        if bingo:
            break

    print(value)
    total += value

print(f'For part two, the total is {total}')