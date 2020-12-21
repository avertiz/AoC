# --- Part Two ---
# As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

# Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. 
# For example, the empty seat below would see eight occupied seats:

# .......#.
# ...#.....
# .#.......
# .........
# ..#L....#
# ....#....
# .........
# #........
# ...#.....
# The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

# .............
# .L.L.#.#.#.#.
# .............
# The empty seat below would see no occupied seats:

# .##.##.
# #.#.#.#
# ##...##
# ...L...
# ##...##
# #.#.#.#
# .##.##.
# Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty 
# (rather than four or more from the previous rules). The other rules still apply: 
# empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

# Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

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
# #.LL.LL.L#
# #LLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLLL.L
# #.LLLLL.L#
# #.L#.##.L#
# #L#####.LL
# L.#.#..#..
# ##L#.##.##
# #.##.#L.##
# #.#####.#L
# ..#.#.....
# LLL####LL#
# #.L#####.L
# #.L####.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##LL.LL.L#
# L.LL.LL.L#
# #.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLL#.L
# #.L#LL#.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.#L.L#
# #.L####.LL
# ..#.#.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.LL.L#
# #.LLLL#.LL
# ..#.L.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
# Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

# Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

import pandas as pd
import copy

def get_above(row, pos, df):
    if row == 0:
        return(0)
    else:
        for r in range(row - 1, -1, -1):
            if df.iloc[r]["seats"][pos] == '#':
                return(1)
            elif df.iloc[r]["seats"][pos] == 'L':
                return(0)
        return(0)

def get_below(row, pos, df):
    if row == len(df)-1:
        return(0)
    else:
        for r in range(row + 1 , len(df), 1):
            if df.iloc[r]["seats"][pos] == '#':
                return(1)
            elif df.iloc[r]["seats"][pos] == 'L':
                return(0)
        return(0)

def get_left(row, pos, df):
    if pos == 0:
        return(0)
    else:
        for p in range(pos - 1, -1, -1):
            if df.iloc[row]["seats"][p] == '#':
                return(1)
            elif df.iloc[row]["seats"][p] == 'L':
                return(0)
        return(0)

def get_right(row, pos, df):
    if pos == len(df.iloc[row]['seats'])-1:
        return(0)
    else:
        for p in range(pos + 1 , len(df.iloc[row]['seats']), 1):
            if df.iloc[row]["seats"][p] == '#':
                return(1)
            elif df.iloc[row]["seats"][p] == 'L':
                return(0)
        return(0)

def get_left_top_diag(row, pos, df):
    if row == 0 or pos == 0:
        return(0)
    else:
        r = row - 1
        p = pos - 1
        for d in range(min([row , pos]) - 1, -1, -1):
            if df.iloc[r]["seats"][p] == '#':
                return(1)
            elif df.iloc[r]["seats"][p] == 'L':
                return(0)
            r -= 1
            p -= 1
        return(0)

def get_right_top_diag(row, pos, df):
    if row == 0 or pos == len(df.iloc[row]['seats'])-1:
        return(0)
    else:
        r = row - 1
        p = pos + 1
        if row == min([row , len(df.iloc[row]['seats'])- 1 - pos]):
            for d in range(row - 1, -1, -1):
                if df.iloc[r]["seats"][p] == '#':
                    return(1)
                elif df.iloc[r]["seats"][p] == 'L':
                    return(0)
                r -= 1
                p += 1
        elif len(df.iloc[row]['seats'])- 1 - pos == min([row , len(df.iloc[row]['seats'])- 1 - pos]):
            for d in range(pos + 1 , len(df.iloc[row]['seats']), 1):
                if df.iloc[r]["seats"][p] == '#':
                    return(1)
                elif df.iloc[r]["seats"][p] == 'L':
                    return(0)
                r -= 1
                p += 1
        return(0)

def get_left_bottom_diag(row, pos, df):
    if row == len(df)-1 or pos == 0:
        return(0)
    else:
        r = row + 1
        p = pos - 1
        if len(df)- 1 - row == min([len(df)- 1 - row , pos]):
            for d in range(row + 1, len(df), 1):
                if df.iloc[r]["seats"][p] == '#':
                    return(1)
                elif df.iloc[r]["seats"][p] == 'L':
                    return(0)
                r += 1
                p -= 1
        elif pos == min([len(df)- 1 - row , pos]):
            for d in range(pos - 1 , -1, -1):
                if df.iloc[r]["seats"][p] == '#':
                    return(1)
                elif df.iloc[r]["seats"][p] == 'L':
                    return(0)
                r += 1
                p -= 1
        return(0)

def get_right_bottom_diag(row, pos, df):
    if row == len(df)-1 or pos == len(df.iloc[row]['seats'])-1:
        return(0)
    else:
        r = row + 1
        p = pos + 1
        if len(df) - 1 - row == min([len(df) - 1 - row , len(df.iloc[row]['seats'])- 1 - pos]):
            for d in range(row + 1, len(df), 1):
                if df.iloc[r]["seats"][p] == '#':
                    return(1)
                elif df.iloc[r]["seats"][p] == 'L':
                    return(0)
                r += 1
                p += 1
        elif len(df.iloc[row]['seats'])- 1 - pos == min([len(df) - 1 - row , len(df.iloc[row]['seats'])- 1 - pos]):
            for d in range(pos + 1 , len(df.iloc[row]['seats']), 1):
                if df.iloc[r]["seats"][p] == '#':
                    return(1)
                elif df.iloc[r]["seats"][p] == 'L':
                    return(0)
                r += 1
                p += 1
        return(0)

def filled_adjacent_seats(left, left_top_diag, above, right_top_diag, right, right_bottom_diag, below, left_bottom_diag):
    if left + left_top_diag + above + right_top_diag + right + right_bottom_diag + below + left_bottom_diag >= 5:
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