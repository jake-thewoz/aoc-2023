import data_getter

data = data_getter.get_data('5_sample').splitlines()
# data = data_getter.get_data(5).splitlines()

# Well this one is a parsing doozey

# I guess we can start by organizing the data into sections

seeds = data[0].split(' ')[1:]
seeds = [int(x) for x in seeds]

# For these, I'm getting the line numbers from looking at the text input file
# btw, I'm naming this 'guide/s' because map is reserved
guides = {}
# guides['seed_soil'] = data[3:51]
# guides['soil_fert'] = data[53:76]
# guides['fert_water'] = data[78:113]
# guides['water_light'] = data[115:138]
# guides['light_temp'] = data[140:155]
# guides['temp_hum'] = data[157:168]
# guides['hum_loc'] = data[170:197]

# These are the sections in the sample
guides['seed_soil'] = data[3:5]
guides['soil_fert'] = data[7:10]
guides['fert_water'] = data[12:16]
guides['water_light'] = data[18:20]
guides['light_temp'] = data[22:25]
guides['temp_hum'] = data[27:29]
guides['hum_loc'] = data[31:33]

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
    print(f'Updating seeds using {key}')
    conversions = updateConv(conversions, guide)

print(f'For part one, the lowest number in locations is {min(conversions)}')

# Part Two ------------------------------------------------------------

# Well holy crap. I guess we can try to brute force this, and only update our seeds
# list with the complete ranges....

new_seeds = []
for x in range(0, len(seeds), 2):
    new_seeds.append(list(range(seeds[x],seeds[x+1]+seeds[x])))

print(new_seeds)


