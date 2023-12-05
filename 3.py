import data_getter

data = data_getter.get_data(3).splitlines()

# This function checks if the coords around a number have a symbol
def isPartNumber(num):
    # These are the [x,y] coordinates of the number we're checking
    coords = list(num.values())[0]

    # Here we'll just go through each coordinate,
    # and then loop through every possible neighbor.
    # and if a neighbor is a non-number, non-period,
    # we'll return true
    for coord in coords:
        for a in range(-1,2):
            for b in range(-1,2):
                # First we need to check for negative indexes,
                # to get around Python's negative indexing
                if coord[0] + a < 0 or coord[1] + b < 0:
                    continue
                # print(f'Checking [{coord[0] + a}, {coord[1] + b}]')

                # We can get around the out-of-bounds by just wrapping in a try except
                try:
                    # This part tripped me up.
                    # Because we're going row by row through the data,
                    # we need to access [x, y] this way: data[y][x]
                    neighbor = data[coord[1] + b][coord[0] + a]
                    if neighbor != '.' and not neighbor.isnumeric():
                        return True
                except:
                    continue

    # If we never found a symbol, we can return false
    return False

# I think it's probably easiest to go row by row

sum = 0
numbers = []

for y in range(len(data)):
    row = data[y]

    # Broadly, we need to:
    # 1. Find the numbers
    # 2. Make sure we have the whole number
    # We'll do this by creating a number object for each number,
    # which includes its coordinates
    coords = []
    num = ''
    for x in range(len(row)):
        if row[x].isnumeric():
            coords.append([x,y])
            num += row[x]
            if x == len(row)-1:
                numbers.append({num: coords}) if num != '' else None
                num = ''
                coords = []
        elif x != 0:
            numbers.append({num: coords}) if num != '' else None
            num = ''
            coords = []
    
# 3. Check if there's a symbol nearby
# 4. And if so, add it to the sum
for num in numbers:
    sum += int(list(num.keys())[0]) if isPartNumber(num) else 0

print(f'The sum of all part numbers is {sum}')

# for dat in data:
#     print(dat)

# Part 2 ---------------------------------------------------

# This will check the coords around the char, and 
# if it touches two seperate partnumbers, will return True
def findRatio(coord):
    good_neighbors = []

    for a in range(-1,2):
        for b in range(-1,2):
            # First we need to check for negative indexes,
            # to get around Python's negative indexing
            if coord[0] + a < 0 or coord[1] + b < 0:
                continue
            # print(f'Checking [{coord[0] + a}, {coord[1] + b}]')

            # We can get around the out-of-bounds by just wrapping in a try except
            try:
                neighbor = [coord[0] + a, coord[1] + b]
                for num in numbers:
                    for val in num.values():
                        for place in val:
                            if neighbor == place and num not in good_neighbors:
                                good_neighbors.append(num)
            except:
                continue
    
    if len(good_neighbors) == 2:
        return int(list(good_neighbors[0].keys())[0]) * int(list(good_neighbors[1].keys())[0])
    else:
        return 0

sumOfRatios = 0

for y in range(len(data)):
    row = data[y]
    for x in range(len(row)):
        char = row[x]

        if not char.isnumeric() and char != '.':
            sumOfRatios += findRatio([x,y])
            
print(f'The sum of all ratios is {sumOfRatios}')
