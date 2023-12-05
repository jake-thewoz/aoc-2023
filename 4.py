import data_getter
import math

# data = data_getter.get_data(4).splitlines()
data = data_getter.get_data('4').splitlines()

# First step, let's clean up the data so we have only what we need
new_data = []
for card in data:
    new_card = card.split(':')[1]
    new_card = new_card.split('|')
    new_card[0] = new_card[0].split(' ')
    new_card[1] = new_card[1].split(' ')
    new_card[0] = set([x for x in new_card[0] if x != ''])
    new_card[1] = set([x for x in new_card[1] if x != ''])
    new_data.append(new_card)
data = new_data

# Now let's just tally up the points
total_points = 0
for card in data:
    if card[0].intersection(card[1]):
        product = math.pow(2, len(card[0].intersection(card[1])) - 1)
        total_points += int(product)

print(f'The total for part one is {total_points}')

# Part Two  -------------------------------------------------

# First, we'll add in a number in front of our sets
# This will represent our count of how many cards we have
for card in data:
    card.insert(0, 1)

for i in range(len(data)):
    current_card = data[i]

    win_count = len(current_card[1].intersection(current_card[2]))

    if win_count > 0:
        for y in range(current_card[0]):
            for x in range(i+1, i+win_count+1):
                data[x][0] += 1

# Now we find the answer
total_cards = 0
for card in data:
    total_cards += card[0]
print(f'The total number of cards for part two is {total_cards}')