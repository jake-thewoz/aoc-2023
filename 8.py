import data_getter

data = data_getter.get_data('8').splitlines()

instructions = data[0]
data = data[2:]

# Formatting the input

new_data = {}

for line in data:
    new_data[line[:3]] = {
        'left': line[7:10],
        'right': line[12:15]
    }

data = new_data

# Part One ---------------------------------------

# We're going to use a simple while loop to iterate through
# the instructions

current_location = 'AAA'
counter = 1
i = 0

while True:
    inst = instructions[i]
    if i == len(instructions) - 1:
        i = 0
    else:
        i += 1
    if inst == 'L':
        current_location = data[current_location]['left']
    if inst == 'R':
        current_location = data[current_location]['right']
    if current_location == 'ZZZ':
        print(f'The number of steps for part one was {counter}')
        break
    else:
        counter += 1

# Part Two -------------------------------------------

# Okay, this doesn't seem much more difficult. First, we'll need to find
# all the starting positions, which end in A

positions = [key for key in data if key[2] == 'A']
print(positions)

# Okay, turns out this was difficult! I'm pretty sure the loop approach
# will eventually get the right answer, but it'll take a LONG time

counter = 1
i = 0
game_over = False

while True:
    inst = instructions[i]

    if i == len(instructions) - 1:
        i = 0
    else:
        i += 1

    for k in range(len(positions)):
        if inst == 'L':
            positions[k] = data[positions[k]]['left']
        if inst == 'R':
            positions[k] = data[positions[k]]['right']
    
    game_over = True
    for position in positions:
        if position[2] != 'Z':
            game_over = False

    if game_over:
        print(f'The number of steps for part two was {counter}')
        break
    else:
        counter += 1
    
    if counter % 1000000 == 0:
        print(f'i: {i}, counter: {counter}, positions: {positions}')