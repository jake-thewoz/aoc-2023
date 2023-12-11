import data_getter

data = data_getter.get_data('11_sample').splitlines()

[print(row) for row in data]

# First step is to expand the data

empty_rows = []
empty_columns = []
# This loop is for the rows
for i in range(len(data)):
    if '#' not in data[i]:
        empty_rows.append(i)

# And now for the columns, we transpose
data = [list(row) for row in zip(*data)]
for i in range(len(data)):
    if '#' not in data[i]:
        empty_columns.append(i)

for i in range(len(empty_columns)):
    data.insert(empty_columns[i] + i, '.' * len(data[i]))

data = [list(row) for row in zip(*data)]
for i in range(len(empty_rows)):
    data.insert(empty_rows[i] + i, list('.' * len(data[i])))

print()
[print(row) for row in data]

