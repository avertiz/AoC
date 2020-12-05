# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your list. 
# However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

# What is the ID of your seat?

import pandas as pd

def range_split(upper, lower):
    value = (upper - lower) / 2 + .5   # probably a better way to do this
    return(value)

def binary_search(range, letters, char, lower, upper):
    if range[1] - range[0] == 1:
        if letters[char] == upper:
            return(range[1])
        elif letters[char] == lower:
            return(range[0])
    else:
        if letters[char] == upper:
            midpoint = range_split(upper = range[1], lower = range[0])
            range = [range[0] + midpoint, range[1]]
        elif letters[char] == lower:
            midpoint = range_split(upper = range[1], lower = range[0])
            range = [range[0], range[1] - midpoint]
        return(binary_search(range = range, letters = letters, char = char + 1, lower = lower, upper = upper)) 

def get_seat(boarding_pass):
    row = binary_search(range = [0,127], letters = boarding_pass[:7], char = 0, lower = 'F', upper = 'B')
    column = binary_search(range = [0,7], letters = boarding_pass[-3:], char = 0, lower = 'L', upper = 'R')
    seat = [int(row), int(column)]
    return(seat)

def get_id(seat):
    id = seat[0] * 8 + seat[1]
    return(id)

def count_values(values):
    count_dict = {}
    for value in values:
        count_dict[value] = values.count(value)
    return(count_dict)

def main():
    input = pd.read_csv('input.csv')
    rows = []
    columns = []
    for key, row in input.iterrows():        
        seat = get_seat(boarding_pass = row['boarding_pass'])
        if seat[0] not in [1, 107]: # remove max and min rows which apparently dont exist
            rows.append(seat[0])
            columns.append(seat[1])
    row_counts = count_values(values = rows)
    columns_counts = count_values(values = columns)
    min_row = min(row_counts, key=row_counts.get)
    min_column = min(columns_counts, key=columns_counts.get)
    my_seat = [min_row, min_column]
    my_id = get_id(seat = my_seat)
    print(my_id)

if __name__ == "__main__":
    main()