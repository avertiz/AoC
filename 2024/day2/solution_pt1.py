def read_input(file:str)->list:
    with open(file=file, mode='r') as f:
        lines = f.readlines()
    input = [x.strip() for x in lines]
    return(input)


def parse_lines(input:list)->list:
    rows = [ [ int(x) for x in row.split(' ') ] for row in input ]
    return(rows)


def check_level(level:list)->bool:
    increasing = True if level[0] < level[1] else False

    for i in range(len(level)-1):
        diff = level[i] - level[i+1]

        if diff == 0 or abs(diff) > 3:
            return(False)

        if increasing and diff > 0:
            return(False)
        
        if not increasing and diff < 0:
            return(False)
        
    return(True)


def safe_levels(levels:list)->list:
    safe_level_list = [check_level(level=x) for x in levels]
    return(safe_level_list)


def main():
    file = '2024/day2/input.txt'
    input = read_input(file=file)
    rows = parse_lines(input=input)
    levels = safe_levels(levels=rows)
    print(sum(levels))


if __name__ == '__main__':
    main()
