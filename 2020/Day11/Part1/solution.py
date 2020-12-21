# --- Day 11: Seating System ---
# Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. 
# As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

# By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. 
# You make a quick map of the seat layout (your puzzle input).

# The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. 
# All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). 
# The following rules are applied to every seat simultaneously:

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.

# After one round of these rules, every seat in the example layout becomes occupied:

# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# After a second round, the seats with four or more occupied adjacent seats become empty again:

# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##
# This process continues for three more rounds:

# #.##.L#.##
# #L###LL.L#
# L.#.#..#..
# #L##.##.L#
# #.##.LL.LL
# #.###L#.##
# ..#.#.....
# #L######L#
# #.LL###L.L
# #.#L###.##
# #.#L.L#.##
# #LLL#LL.L#
# L.L.L..#..
# #LLL.##.L#
# #.LL.LL.LL
# #.LL#L#.##
# ..L.L.....
# #L#LLLL#L#
# #.LLLLLL.L
# #.#L#L#.##
# #.#L.L#.##
# #LLL#LL.L#
# L.#.L..#..
# #L##.##.L#
# #.#L.LL.LL
# #.#L#L#.##
# ..L.L.....
# #L#L##L#L#
# #.LLLLLL.L
# #.#L#L#.##
# At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, 
# you count 37 occupied seats.

# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

import pandas as pd
import copy

def get_above(row, pos, df):
    if row == 0:
        return(0)
    else:
        above = df.iloc[row-1]["seats"][pos]
        if above in ['L', '.']:
            return(0)
        elif above == '#':
            return(1)

def get_below(row, pos, df):
    if row == len(df)-1:
        return(0)
    else:
        below = df.iloc[row+1]["seats"][pos]
        if below in ['L', '.']:
            return(0)
        elif below == '#':
            return(1)

def get_left(row, pos, df):
    if pos == 0:
        return(0)
    else:
        left = df.iloc[row]["seats"][pos-1]
        if left in ['L', '.']:
            return(0)
        elif left == '#':
            return(1)

def get_right(row, pos, df):
    if pos == len(df.iloc[row]['seats'])-1:
        return(0)
    else:
        right = df.iloc[row]["seats"][pos+1]
        if right in ['L', '.']:
            return(0)
        elif right == '#':
            return(1)

def get_left_top_diag(row, pos, df):
    if row == 0 or pos == 0:
        return(0)
    else:
        left_top_diag = df.iloc[row-1]["seats"][pos-1]
        if left_top_diag in ['L', '.']:
            return(0)
        elif left_top_diag == '#':
            return(1)

def get_right_top_diag(row, pos, df):
    if row == 0 or pos == len(df.iloc[row]['seats'])-1:
        return(0)
    else:
        right_top_diag = df.iloc[row-1]["seats"][pos+1]
        if right_top_diag in ['L', '.']:
            return(0)
        elif right_top_diag == '#':
            return(1)

def get_left_bottom_diag(row, pos, df):
    if row == len(df)-1 or pos == 0:
        return(0)
    else:
        left_bottom_diag = df.iloc[row+1]["seats"][pos-1]
        if left_bottom_diag in ['L', '.']:
            return(0)
        elif left_bottom_diag == '#':
            return(1)

def get_right_bottom_diag(row, pos, df):
    if row == len(df)-1 or pos == len(df.iloc[row]['seats'])-1:
        return(0)
    else:
        right_bottom_diag = df.iloc[row+1]["seats"][pos+1]
        if right_bottom_diag in ['L', '.']:
            return(0)
        elif right_bottom_diag == '#':
            return(1)

def filled_adjacent_seats(left, left_top_diag, above, right_top_diag, right, right_bottom_diag, below, left_bottom_diag):
    if left + left_top_diag + above + right_top_diag + right + right_bottom_diag + below + left_bottom_diag >= 4:
        return(True)
    else:
        return(False)

def empty_adjacent_seats(left, left_top_diag, above, right_top_diag, right, right_bottom_diag, below, left_bottom_diag):
    if left + left_top_diag + above + right_top_diag + right + right_bottom_diag + below + left_bottom_diag == 0:
        return(True)
    else:
        return(False)

def empty_seat():
    return('L')

def fill_seat():
    return('#')

def create_map(df):

    new_map = copy.copy(df)

    for row in range(len(df)):
        for pos in range(len(df.iloc[row]['seats'])):

            if df.iloc[row]['seats'][pos] != '.':

                left = get_left(row = row, pos = pos, df = df)
                left_top_diag = get_left_top_diag(row = row, pos = pos, df = df)
                above = get_above(row = row, pos = pos, df = df)
                right_top_diag = get_right_top_diag(row = row, pos = pos, df = df)
                right = get_right(row = row, pos = pos, df = df)
                right_bottom_diag = get_right_bottom_diag(row = row, pos = pos, df = df)
                below = get_below(row = row, pos = pos, df = df)
                left_bottom_diag = get_left_bottom_diag(row = row, pos = pos, df = df)

                if df.iloc[row]['seats'][pos] == 'L':

                    if empty_adjacent_seats(left, left_top_diag, above, right_top_diag, right, right_bottom_diag, below, left_bottom_diag):
                        row_list = list(new_map.iloc[row]["seats"])
                        row_list[pos] = fill_seat()
                        row_string = ''.join(row_list)
                        new_map.iloc[row]["seats"] = row_string

                if df.iloc[row]['seats'][pos] == '#':

                    if filled_adjacent_seats(left, left_top_diag, above, right_top_diag, right, right_bottom_diag, below, left_bottom_diag):
                        row_list = list(new_map.iloc[row]["seats"])
                        row_list[pos] = empty_seat()
                        row_string = ''.join(row_list)
                        new_map.iloc[row]["seats"] = row_string
    
    return(new_map)

def count_occupied_seats(df):
    seat_count = 0
    for key, row in df.iterrows():
        seat_count += row['seats'].count('#')
    return(seat_count)

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    current_map = input
    new_map = create_map(df = current_map)
    while not current_map.equals(new_map):
        current_map = copy.copy(new_map)
        new_map = create_map(df = current_map)
        new_map.to_csv('new_map.csv', index = False)
    
    occupied_seats = count_occupied_seats(df = new_map)
    print(occupied_seats)

if __name__ == "__main__":
    main()