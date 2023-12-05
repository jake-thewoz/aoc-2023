import data_getter

data = data_getter.get_data(2).splitlines()

new_data = []
for line in data:
    new_line = line.split(':')
    new_line[1] = new_line[1].split(';')
    new_line[0] = int(new_line[0].split(' ')[1])
    new_data.append(new_line)
data = new_data

# Part One

total = 0
for line in data:
    valid_game = True
    for game in line[1]:
        draws = game.split(',')
        for draw in draws:
            if int(draw.split(' ')[-2]) > 14:
                valid_game = False
            elif int(draw.split(' ')[-2]) == 14 and 'blue' not in draw:
                valid_game = False
            elif int(draw.split(' ')[-2]) == 13 and 'green' not in draw and 'blue' not in draw:
                valid_game = False
        if not valid_game:
            break
            
    if valid_game:
        total += line[0]

print(f'The total for part one is {total}')

# Part Two

# First lets remove the game number from every element in the list,
# so we're left with only the relevant info

new_data = []
for line in data:
    new_data.append(line[1])
data = new_data

sum_power = 0
for line in data:
    blue, red, green = -1, -1, -1

    for draw in line:
        for pull in draw.split(','):
            if 'blue' in pull and int(pull.split(' ')[1]) > blue:
                blue = int(pull.split(' ')[1])
            if 'red' in pull and int(pull.split(' ')[1]) > red:
                red = int(pull.split(' ')[1])
            if 'green' in pull and int(pull.split(' ')[1]) > green:
                green = int(pull.split(' ')[1])

    power = red * blue * green
    sum_power += power

print(f'The total for part two is {sum_power}')