import data_getter

data = data_getter.get_data('9').splitlines()

# Data prep

new_data = []
for row in data:
    new_row = row.split(' ')
    new_row = [int(num) for num in new_row]
    new_data.append(new_row)
data = new_data

[print(row) for row in data]
print()

# Part One ------------------------------------

answers = []

for row in data:
    differences = []
    differences.append(row)
    not_all_zeroes = True
    current_row = row

    while not_all_zeroes:
        new_diff = []

        for i in range(1, len(current_row)):
            new_diff.append(current_row[i] - current_row[i-1])

        if set(new_diff) == {0}:
            not_all_zeroes = False
        
        differences.append(new_diff)
        current_row = new_diff

    answer = 0
    for row in differences:
        answer += row[-1]
    
    answers.append(answer)

print(f'The sum of all values for part one is {sum(answers)}')    