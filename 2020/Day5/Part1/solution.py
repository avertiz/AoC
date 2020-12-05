# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your boarding pass! 
# You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); 
# perhaps you can find your seat through process of elimination.

# Instead of zones or groups, this airline uses binary space partitioning to seat people. 
# A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). 
# Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; 
# the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). 
# The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of FBFBBFFRLR:

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). 
# The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

# Here are some other boarding passes:

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

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

def main():
    input = pd.read_csv('input.csv')
    seats_ids = {}
    for key, row in input.iterrows():
        seat = get_seat(boarding_pass = row['boarding_pass'])
        id = get_id(seat = seat)
        seats_ids[id] = seat
    ids = seats_ids.keys()
    max_id = max(ids)
    print(max_id)

if __name__ == "__main__":
    main()