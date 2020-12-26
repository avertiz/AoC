# --- Part Two ---
# Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

# Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

# For example, using the same instructions as above:

# F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. 
# The waypoint stays 10 units east and 1 unit north of the ship.
# N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
# F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. 
# The waypoint stays 10 units east and 4 units north of the ship.
# R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
# F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. 
# The waypoint stays 4 units east and 10 units south of the ship.
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

# Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

import pandas as pd

def turn_waypoint(current_instruction, waypoint):
    dir_dict_clockwise = {'E':['S','W','N'], 'S':['W','N','E'], 'W':['N','E','S'], 'N':['E','S','W']}
    dir_dict_counter_clockwise = {'E':['N','W','S'], 'S':['E','N','W'], 'W':['S','E','N'], 'N':['W','S','E']}
    key1 = list(waypoint.keys())[0]
    key2 = list(waypoint.keys())[1]
    if current_instruction[0] == 'L':
        if current_instruction[1:] == '90':
            waypoint = {dir_dict_counter_clockwise[key1][0]:waypoint[key1], dir_dict_counter_clockwise[key2][0]:waypoint[key2]}
        elif current_instruction[1:] == '180':
            waypoint = {dir_dict_counter_clockwise[key1][1]:waypoint[key1], dir_dict_counter_clockwise[key2][1]:waypoint[key2]}
        elif current_instruction[1:] == '270':
            waypoint = {dir_dict_counter_clockwise[key1][2]:waypoint[key1], dir_dict_counter_clockwise[key2][2]:waypoint[key2]}
    elif current_instruction[0] == 'R':
        if current_instruction[1:] == '90':
            waypoint = {dir_dict_clockwise[key1][0]:waypoint[key1], dir_dict_clockwise[key2][0]:waypoint[key2]}            
        elif current_instruction[1:] == '180':
            waypoint = {dir_dict_clockwise[key1][1]:waypoint[key1], dir_dict_clockwise[key2][1]:waypoint[key2]}
        elif current_instruction[1:] == '270':
            waypoint = {dir_dict_clockwise[key1][2]:waypoint[key1], dir_dict_clockwise[key2][2]:waypoint[key2]}
    return(waypoint)

def move_waypoint(current_instruction, waypoint):
    dir_dict_reverse = {'E':'W', 'S':'N', 'W':'E', 'N':'S'}
    dir_dict_multiplyer = {'E':{'N':0, 'S':0, 'E':1, 'W':-1},
                           'S':{'N':-1, 'S':1, 'E':0, 'W':0},
                           'W':{'N':0, 'S':0, 'E':-1, 'W':1},
                           'N':{'N':1, 'S':-1, 'E':0, 'W':0}}
    direction = current_instruction[0]
    movement = int(current_instruction[1:])    
    key1 = list(waypoint.keys())[0]
    key2 = list(waypoint.keys())[1]
    waypoint[key1] += dir_dict_multiplyer[key1][direction] * movement
    waypoint[key2] += dir_dict_multiplyer[key2][direction] * movement
    if waypoint[key1] < 0:
        waypoint[dir_dict_reverse[key1]] = -1 * waypoint.pop(key1)
    if waypoint[key2] < 0:
        waypoint[dir_dict_reverse[key2]] = -1 * waypoint.pop(key2)
    return(waypoint)

def move_ship(current_instruction, current_location, waypoint):
    dir_dict_reverse = {'E':'W', 'S':'N', 'W':'E', 'N':'S'}
    dir_dict_multiplyer = {'E':{'N':0, 'S':0, 'E':1, 'W':-1},
                           'S':{'N':-1, 'S':1, 'E':0, 'W':0},
                           'W':{'N':0, 'S':0, 'E':-1, 'W':1},
                           'N':{'N':1, 'S':-1, 'E':0, 'W':0}}
    movement = int(current_instruction[1:])
    ship_key1 = list(current_location.keys())[0]
    ship_key2 = list(current_location.keys())[1]
    waypoint_key1 = list(waypoint.keys())[0]
    waypoint_key2 = list(waypoint.keys())[1]
    current_location[ship_key1] += dir_dict_multiplyer[ship_key1][waypoint_key1] * movement * waypoint[waypoint_key1]
    current_location[ship_key1] += dir_dict_multiplyer[ship_key1][waypoint_key2] * movement * waypoint[waypoint_key2]
    current_location[ship_key2] += dir_dict_multiplyer[ship_key2][waypoint_key1] * movement * waypoint[waypoint_key1]
    current_location[ship_key2] += dir_dict_multiplyer[ship_key2][waypoint_key2] * movement * waypoint[waypoint_key2]
    if current_location[ship_key1] < 0:
        current_location[dir_dict_reverse[ship_key1]] = -1 * current_location.pop(ship_key1)
    if current_location[ship_key2] < 0:
        current_location[dir_dict_reverse[ship_key2]] = -1 * current_location.pop(ship_key2)
    return(current_location)
    
def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    location = {'N':0, 'E':0}
    waypoint = {'N':1, 'E':10}
    for key, row in input.iterrows():
        if row['instructions'][0] in ['L', 'R']:
            waypoint = turn_waypoint(current_instruction = row['instructions'], waypoint = waypoint)
        elif row['instructions'][0] in ['N', 'S', 'E', 'W']:
            waypoint = move_waypoint(current_instruction = row['instructions'], waypoint = waypoint)
        elif row['instructions'][0] == 'F':
            location = move_ship(current_instruction = row['instructions'], current_location = location, waypoint = waypoint)
            print(location)
    dir1 = list(location.values())[0]
    dir2 = list(location.values())[1]
    answer = dir1 + dir2
    print(answer)

if __name__ == "__main__":
    main()