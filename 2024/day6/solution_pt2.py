from solution_pt1 import read_input, get_guard_position, move_guard

def get_obstacles(input:list)->list:
    obstacles = []
    for row_num, row in enumerate(input):
        for col_num, character in enumerate(row):
            if character == '#':
                obstacles.append([row_num, col_num])
    return(obstacles)


file        = '/home/av91203/python/wb_eod_pricing/2024/day6/input.txt'
input       = read_input(file=file)
direction_map = {
        '^' : [-1, 0 ,'>'],
        '>' : [0 , 1 ,'v'],
        'v' : [1 , 0 ,'<'],
        '<' : [0 ,-1 ,'^'],
}
obstacles   = get_obstacles(input=input)
guard_position = get_guard_position(input=input, direction_map=direction_map)
