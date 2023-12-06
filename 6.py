import data_getter

data = data_getter.get_data('6').splitlines()

# Part One -------------------------------------------

# This seems simple enough. I think we can do this with some
# for-loops and counters

# First, we have to get the data how we want it

times = data[0].split()[1:]
distances = data[1].split()[1:]
times = [int(x) for x in times]
distances = [int(x) for x in distances]

# Then let's try looping through the numbers

number_of_ways = []

for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    ways = 0
    for x in range(time):
        if (time - x) * x > distance:
            ways += 1
    
    number_of_ways.append(ways)

# This is the cleanest way I've found to multiply all
# items in a list together, without using external libraries

margin_of_error = 1

for way in number_of_ways:
    margin_of_error *= way

print(f'The margin of error for part one is {margin_of_error}')

# Part Two --------------------------------------------------

# Okay, so it's the same thing with just one really big set of numbers
# Let's grab the data differently

times = data[0].split()[1:]
distances = data[1].split()[1:]
time = int(''.join(times))
distance = int(''.join(distances))

# First, I'll try the old loop method

ways = 0
for x in range(time):
    if (time - x) * x > distance:
        ways += 1

print(f'The number of different ways for part two is {ways}')