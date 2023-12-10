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
diff_list = []

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
    diff_list.append(differences)

print(f'The sum of all values for part one is {sum(answers)}')

# Part Two ------------------------------------------------------------

# This is kinda the same problem

second_answer = 0
for diff in diff_list:
    subtractor = 0
    for i in range(-2, -len(diff), -1):
        subtractor = diff[i][0] - subtractor
    second_answer += diff[0][0] - subtractor
print(f'The sum of beginning numbers for part two is {second_answer}')