import data_getter

data = data_getter.get_data('10_sample').splitlines()

[print(row) for row in data]
print()

# Part One ------------------------------------------

# There's certainly a solution for this that uses sets.
# I think I'll try keeping track of all visited tiles
# with a set of tuples (since you cannot have a set of lists)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 'S':
            start = (x, y) # this is a lazy way to init a variable, but it actually works

print(f'Starting position is {start}')

# You know what, I'm going to transpose the data so I can access it in (x, y) instead of (y, x)
data = [list(row) for row in zip(*data)]
print_data = [list(row) for row in zip(*data)]

# This is our set of visited tiles
visited = set()
visited.add(start)

# Now that we have the start, we want to find the two first directions

two_tiles = set()

# Here are the possible connections to any tile, labeled for north, south, east, west
w_options = '-LF'
e_options = '-7J'
n_options = '|7F'
s_options = '|LJ'

if (data[start[0] - 1][start[1]]) in w_options:
    two_tiles.add((start[0] - 1, start[1]))
if (data[start[0] + 1][start[1]]) in e_options:
    two_tiles.add((start[0] + 1, start[1]))
if (data[start[0]][start[1] - 1]) in n_options:
    two_tiles.add((start[0], start[1] - 1))
if (data[start[0]][start[1] + 1]) in s_options:
    two_tiles.add((start[0], start[1] + 1))

print(two_tiles)    
visited.update(two_tiles)

# Now we'll make a tool for finding the next tile
def find_next(tile, previous_tiles):
    # Here I'll couch these with exceptions, so we don't accidentally do
    # negative indexing or index out of bounds
    if tile[0] != 0:
        if (data[tile[0] - 1][tile[1]]) in w_options and ((tile[0] - 1, tile[1])) not in previous_tiles:
            return ((tile[0] - 1, tile[1]))
    if tile[0] != len(data) - 1:
        if (data[tile[0] + 1][tile[1]]) in e_options and ((tile[0] + 1, tile[1])) not in previous_tiles:
            return ((tile[0] + 1, tile[1]))
    if tile[1] != 0:
        if (data[tile[0]][tile[1] - 1]) in n_options and ((tile[0], tile[1] - 1)) not in previous_tiles:
            return ((tile[0], tile[1] - 1))
    if tile[1] != len(data[0]) - 1:
        if (data[tile[0]][tile[1] + 1]) in s_options and ((tile[0], tile[1] + 1)) not in previous_tiles:
            return ((tile[0], tile[1] + 1))

def update_print_data(visited):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if (x, y) in visited:
                print_data[y][x] = 'X'

def print_the_data():
    for row in print_data:
        print(row)


# Here's our main loop to go through the pipes
done = False
count = 1
current_tiles = set(two_tiles)

while not done:
    visited.update(current_tiles)
    print(f'Visited tiles: {visited}')
    print(f'Current tiles: {current_tiles}')
    update_print_data(visited)
    print_the_data()
    first = find_next(list(current_tiles)[0], visited)
    second = find_next(list(current_tiles)[1], visited)
    count += 1
    current_tiles = set()
    current_tiles.add(first)
    current_tiles.add(second)
    x = input()

    if len(current_tiles) == 1:
        done = True

print(f'The count for part one is {count}')