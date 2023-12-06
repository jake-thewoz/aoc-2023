import data_getter

data = data_getter.get_data('5').splitlines()
# data = data_getter.get_data('5_sample').splitlines()

# Well this one is a parsing doozey

# I guess we can start by organizing the data into sections

seeds = data[0].split(' ')[1:]
seeds = [int(x) for x in seeds]

guides = {}

# These are hardcoded from my input data, so they may not work for everyone

guides['seed_soil'] = data[3:51]
guides['soil_fert'] = data[53:76]
guides['fert_water'] = data[78:113]
guides['water_light'] = data[115:138]
guides['light_temp'] = data[140:155]
guides['temp_hum'] = data[157:168]
guides['hum_loc'] = data[170:197]

# These are the sections in the sample

# guides['seed_soil'] = data[3:5]
# guides['soil_fert'] = data[7:10]
# guides['fert_water'] = data[12:16]
# guides['water_light'] = data[18:20]
# guides['light_temp'] = data[22:25]
# guides['temp_hum'] = data[27:29]
# guides['hum_loc'] = data[31:33]

# Now I just want to turn them all into ints,
# and make each row a list
for guide in guides:
    for i in range(len(guides[guide])):
        guides[guide][i] = guides[guide][i].split(' ')
        guides[guide][i] = [int(x) for x in guides[guide][i]]

print(f'So we start with {len(seeds)} seeds...')

# I'll rename this to conversions;
# we don't seem to need any of the seed numbers by the end of it (maybe in part two)
# so I'll just update this 'conversions' list with the new numbers as we go
conversions = seeds

# This function will update conversion table using the provided guide
def updateConv(conv, guide):
    for s in range(len(conv)):
        seed = conv[s]
        for rule in guide:
            # This is the fastest way to figure out if an integer is in
            # a range of integers
            if rule[1] <= seed <= rule[1] + rule[2]:
                conv[s] = rule[0] + (seed - rule[1])
    return conv

for key in guides:
    guide = guides[key]
    # print(f'Updating seeds using {key}')
    conversions = updateConv(conversions, guide)

print(f'For part one, the lowest number in locations is {min(conversions)}')

# Part Two ------------------------------------------------------------

# After thinking about this, the easiest solution I can think of is to 
# create a series of range borders, so if we have a number like:
# '10 15' - instead of keeping a list of [10, 11, 12, ...24], we just keep
# track of the borders, so [10, 24]. Then we should be able to do simple
# math for each of the mapping instructions

# This time I'll call my main list 'spans', since they're ranges of seed values
seeds = data[0].split(' ')[1:]
seeds = [int(x) for x in seeds]

spans = []
for i in range(0, len(seeds), 2):
    span = []
    span.append(seeds[i])
    span.append(seeds[i] + seeds[i+1] - 1)
    spans.append(span)

for key in guides:
    guide = guides[key]
    for rule in guide:
        # To make this easier, I'm adding a number to the rules:
        # The new number will be the upper-bound of the rule range,
        # which correlates to span[1], or the upper-bound of the span
        rule.append(rule[1] + rule[2] - 1)
        # This next rule will be our 'transform' rule
        rule.append(rule[0] - rule[1])


for key in guides:
    guide = guides[key]

    # This is our list that we'll use to update our spans list.
    # Every time we use a rule to translate a portion of a span,
    # we add that new span to this list. After going through all
    # the rules, we replace our span list with this.
    new_spans = []

    for span in spans:
        # Here we'll make a copy of the current span, because we need to save the state of
        # each span as it is mangled by the rules
        current_spans = [span[:]]

        # Now we need a while loop, because current_spans acts as a buffer which can be added to
        i = 0
        while i < len(current_spans):
            # Then we go through the rules, applying them to the span in the buffer
            c_span = current_spans[i]

            # This is for an exception, where the new_spans list wouldn't be populated
            # if a span was affected by none of the rules
            special_span = True

            for rule in guide:
                # We're gonna have to account for six cases (I think)

                # 1. Rule is completely below span
                if rule[3] < c_span[0]:
                    continue
                # 2. Rule is completely above span
                if rule[1] > c_span[1]:
                    continue
                # 3. Rule is half below span (so span needs to change)
                if rule[1] < c_span[0] and rule[3] <= c_span[1]:
                    special_span = False
                    low_span_length = rule[3] - c_span[0] + 1
                    high_span_length = c_span[1] - rule[3]
                    new_spans.append([c_span[0] + rule[4], c_span[0] + low_span_length + rule[4] - 1])
                    current_spans.append([rule[3] + 1, c_span[1]]) if rule[3] < c_span[1] else None
                    break
                # 4. Rule is half above span (so span needs to change)
                if rule[1] >= c_span[0] and rule[3] > c_span[1]:
                    special_span = False
                    low_span_length = rule[1] - c_span[0]
                    high_span_length = c_span[1] - rule[1] + 1
                    current_spans.append([c_span[0], c_span[0] + low_span_length - 1]) if c_span[0] < rule[1] else None
                    new_spans.append([rule[0], rule[0] + high_span_length - 1])
                    break
                # 5. Rule is entirely inside of span (or equal)
                if rule[1] >= c_span[0] and rule[3] <= c_span[1]:
                    special_span = False
                    low_span_length = rule[1] - c_span[0]
                    mid_span_length = rule[2]
                    high_span_length = c_span[1] - rule[3]
                    current_spans.append([c_span[0], c_span[0] + low_span_length - 1]) if c_span[0] < rule[1] else None
                    new_spans.append([rule[0], rule[0] + mid_span_length - 1])
                    current_spans.append([rule[3] + 1, c_span[1]]) if c_span[1] > rule[3] else None
                    break
                # 6. Span is entirely inside of rule
                if rule[1] < c_span[0] and rule[3] > c_span[1]:
                    special_span = False
                    span_length = c_span[1] - c_span[0] + 1
                    new_spans.append([c_span[0] + rule[4], c_span[1] + rule[4]])

            # This is our special case from before, which happens if a span was completely
            # untouched by all the rules in a set
            new_spans.append(c_span) if special_span else None

            i += 1

    # And here we replace our old spans with the new ones
    spans = new_spans

# Now our spans list has the final ranges of all soil locations!
# Here we just grab the lowest value
lowest_location = min(x[0] for x in spans)

print(f'The lowest location number for part two is {lowest_location}')