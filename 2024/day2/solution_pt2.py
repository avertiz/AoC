from solution_pt1 import read_input, parse_lines, check_level

def dampener(level:list)->bool:
    result = check_level(level=level)

    if not result:
        for i, _ in enumerate(level):
            dampened_level:list = level.copy()
            dampened_level.pop(i)
            result = check_level(level=dampened_level)
            if result:
                return(result)
        return(False)

    return(result)


def safe_levels(levels:list)->list:
    safe_level_list = [dampener(level=x) for x in levels]
    return(safe_level_list)


def main():

    file = '2024/day2/input.txt'
    input = read_input(file=file)
    rows = parse_lines(input=input)
    levels = safe_levels(levels=rows)
    print(sum(levels))


if __name__ == '__main__':
    main()
