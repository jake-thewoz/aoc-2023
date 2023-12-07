import data_getter

data = data_getter.get_data('7').splitlines()

# Here we'll prep our deck for later use
deck = data[:]
deck = [x.split(' ') for x in deck]

# Part One ----------------------------------------------

# Okay, well this seems simple enough!

# In research, I've discovered that python does NOT have a sorting function
# that accepts a comparison function as an argument.

# That is annoying, but since this is AoC, this will be good practice to 
# implement a sorting algorithm myself.

# I've chosen quick sort. Wish me luck.

# To start, here are my functions for determing what kind of hand it is:
def rankHand(hand):
    # Five of a kind
    if len(set(hand)) == 1:
        return 7
    # Four of a kind
    if len(set(hand)) == 2:
        if hand.count(list(set(hand))[0]) == 4 or hand.count(list(set(hand))[0]) == 1:
            return 6
        # Full house
        if hand.count(list(set(hand))[0]) == 3 or hand.count(list(set(hand))[0]) == 2:
            return 5
    # Three of a kind
    if len(set(hand)) == 3:
        for card in hand:
            if hand.count(card) == 3:
                return 4
        # Two pair
        if hand.count(list(set(hand))[0]) == 2 or hand.count(list(set(hand))[1]) == 2:
            return 3
    # One pair
    if len(set(hand)) == 4:
        return 2
    # Nothing
    if len(set(hand)) == 5:
        return 1
    # default return... is this needed?
    return 0

# Here's a function for ranking the individual cards
# (in case of tied hands)
def rankCard(card):
    if not card.isnumeric():
        if card == 'T':
            return 10
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        else: # This is the ace
            return 14
    else:
        return int(card)

# Now, here's my comparison function
def compare(x, y):
    if rankHand(x) < rankHand(y):
        return True
    elif rankHand(x) > rankHand(y):
        return False
    else: # They must be equal
        for c in range(5):
            if rankCard(x[c]) < rankCard(y[c]):
                return True
            elif rankCard(x[c]) > rankCard(y[c]):
                return False
    
    # If the hands are trully equal, I guess we return true?
    return True

# Here is my quick sort implementation, with the custom comparison
def quickSort(deck, compare):
    quickSortHelper(deck, 0, len(deck) - 1, compare)

def quickSortHelper(deck, first, last, compare):
    if first < last:
        splitpoint = partition(deck, first, last, compare)

        quickSortHelper(deck, first, splitpoint - 1, compare)
        quickSortHelper(deck, splitpoint + 1, last, compare)

def partition(deck, first, last, compare):
    pivotvalue = deck[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and compare(deck[leftmark][0], pivotvalue[0]):
            leftmark = leftmark + 1

        while rightmark >= leftmark and not compare(deck[rightmark][0], pivotvalue[0]):
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            deck[leftmark], deck[rightmark] = deck[rightmark], deck[leftmark]

    deck[first], deck[rightmark] = deck[rightmark], deck[first]

    return rightmark

# Now all that's left to do is to sort our deck!
quickSort(deck, compare)

# Now we calculate the total winnings :)
winnings = 0
for i in range(len(deck)):
    bid = int(deck[i][1])
    winnings += bid * (i+1)

print(f'The total winnings for part one is {winnings}')

# Part Two --------------------------------------------------------------

# Okay, this isn't so bad. All we have to do now is modify our rankHand function
# to account for these 'jokers wild' rules.

def jRankHand(hand):
    # If there's no J, we can call our other function
    if 'J' not in hand:
        return rankHand(hand)
    elif 'J' in hand and len(set(hand)) == 1:
        # this is a DEVIOUS exception
        return rankHand(hand)

    # We'll make a modified version of the hand, then just pass it to our
    # normal ranking function
    modifiedHand = hand[:]

    # In order to find the most common card that isn't J, we need to make a hand
    # that has J removed
    handWithoutJ = [card for card in hand if card != 'J']
    # Then we can find the best option for J to become
    mostCommonCard = max(handWithoutJ, key=handWithoutJ.count)

    # Then we replace J in our new hand with this option
    modifiedHand = modifiedHand.replace('J', mostCommonCard)

    # ...and simply call our old rankHand with the new hand
    return rankHand(modifiedHand)

def jRankCard(card):
    if not card.isnumeric():
        if card == 'T':
            return 10
        elif card == 'J':
            return 1
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        else: # This is the ace
            return 14
    else:
        return int(card)

# Now we need a modified compare, which will use this new jRankHand()

def jCompare(x, y):
    if jRankHand(x) < jRankHand(y):
        return True
    elif jRankHand(x) > jRankHand(y):
        return False
    else: # They must be equal
        for c in range(5):
            if jRankCard(x[c]) < jRankCard(y[c]):
                return True
            elif jRankCard(x[c]) > jRankCard(y[c]):
                return False
    
    # If the hands are trully equal, I guess we return true?
    # Actually, it doesn't seem to matter either way
    return False

# Here goes nothing! Hopefully this works first time :)
quickSort(deck, jCompare)

# Now we calculate the total winnings :)
winnings = 0
for i in range(len(deck)):
    bid = int(deck[i][1])
    winnings += bid * (i+1)

print(f'The total winnings for part two is {winnings}')