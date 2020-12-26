# --- Day 12: Rain Risk ---
# Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

# Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, 
# it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

# The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. 
# After staring at them for a few minutes, you work out what they probably mean:

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. 
# (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

# For example:

# F10
# N3
# F7
# R90
# F11
# These instructions would be handled as follows:

# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) 
# from its starting position is 17 + 8 = 25.

# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

import pandas as pd

def turn_ship(current_instruction, current_direction):
    dir_dict = {'E':0, 'S':90, 'W':180, 'N':270}
    key_list = list(dir_dict.keys())
    val_list = list(dir_dict.values())
    if current_instruction[0] == 'L':
        rotation = dir_dict[current_direction] + 360 - int(current_instruction[1:])
        if rotation >= 360:
            rotation -= 360
        position = val_list.index(rotation)
        new_dir = key_list[position]
    elif current_instruction[0] == 'R':
        rotation = dir_dict[current_direction] + int(current_instruction[1:])
        if rotation >= 360:
            rotation -= 360
        position = val_list.index(rotation)
        new_dir = key_list[position]
    return(new_dir)

def move_ship(current_instruction, current_direction):
    if current_instruction[0] in ['E', 'N']:
        direction = int(current_instruction[1:])
    elif current_instruction[0] in ['W', 'S']:
        direction = -int(current_instruction[1:])
    elif current_instruction[0] == 'F':
        if current_direction in ['E', 'N']:
            direction = int(current_instruction[1:])
        elif current_direction in ['W', 'S']:
            direction = -int(current_instruction[1:])
    return(direction)
    
def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    current_direction = 'E'
    east_west = 0
    north_south = 0
    for key, row in input.iterrows():
        if row['instructions'][0] in ['L', 'R']:
            current_direction = turn_ship(current_instruction = row['instructions'], current_direction = current_direction)
        elif row['instructions'][0] in ['N', 'S']:
            north_south += move_ship(current_instruction = row['instructions'], current_direction = current_direction)
        elif row['instructions'][0] in ['E', 'W']:
            east_west += move_ship(current_instruction = row['instructions'], current_direction = current_direction)
        elif row['instructions'][0] == 'F':
            if current_direction in ['N', 'S']:
                north_south += move_ship(current_instruction = row['instructions'], current_direction = current_direction)
            elif current_direction in ['E', 'W']:
                east_west += move_ship(current_instruction = row['instructions'], current_direction = current_direction)
    east_west = abs(east_west)
    north_south = abs(north_south)
    answer = east_west + north_south
    print(answer)

if __name__ == "__main__":
    main()