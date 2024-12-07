def read_input(file:str)->list:
    with open(file=file, mode='r') as f:
        lines = f.readlines()
    input = [x.strip() for x in lines]
    return(input)


def get_guard_position(input:list, direction_map:dict)->list:
    for row_num, row in enumerate(input):
        for col_num, col in enumerate(row):
            if col in direction_map.keys():
                return([col, [row_num, col_num]])


def move_guard(input:list, guard_position:list, direction_map:dict)->list:
    direction = guard_position[0]

    potential_new_position = [ 
        direction,
        [ guard_position[1][0] + direction_map[direction][0], guard_position[1][1] + direction_map[direction][1] ]
    ]

    if potential_new_position[1][0] < 0 or potential_new_position[1][1] < 0:
        return(-1) 

    try:
        input[ potential_new_position[1][0] ][ potential_new_position[1][1] ]
    except IndexError:
        return(-1)

    if input[ potential_new_position[1][0] ][ potential_new_position[1][1] ] == '#':
        new_direction = direction_map[direction][2]
        new_position  = move_guard(input=input,
                                   guard_position=[new_direction, guard_position[1]],
                                   direction_map=direction_map)
    else:
        new_position = potential_new_position

    return(new_position)


def main():
    file        = '2024/day6/input.txt'
    input       = read_input(file=file)
    solution    = input.copy()
    direction_map = {
        '^' : [-1, 0 ,'>'],
        '>' : [0 , 1 ,'v'],
        'v' : [1 , 0 ,'<'],
        '<' : [0 ,-1 ,'^'],
    }
    guard_position = get_guard_position(input=input, direction_map=direction_map)
    row_str = solution[ guard_position[1][0] ]
    col     = guard_position[1][1]
    solution[ guard_position[1][0] ] =  row_str[:col] + 'X' + row_str[col + 1:]

    while guard_position != -1:
        row_str = solution[ guard_position[1][0] ]
        col     = guard_position[1][1]
        solution[ guard_position[1][0] ] =  row_str[:col] + 'X' + row_str[col + 1:]
        guard_position = move_guard(input=input, guard_position=guard_position, direction_map=direction_map)

    count = 0
    for _, row in enumerate(solution):
        for _, character in enumerate(row):
            if character == 'X':
                count += 1

    print(count)

if __name__ == '__main__':
    main()
