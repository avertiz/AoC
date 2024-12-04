from typing import Dict, List


def read_input(file:str)->list:
    with open(file=file, mode='r') as f:
        lines = f.readlines()
    input = [x.strip() for x in lines]
    return(input)


def create_row_list(input:list, min_max_indexes:Dict[str, int])->list:
    row_list = ['' for x in range(min_max_indexes['width'])]
    for _, row in enumerate(input):
        for col_num, col in enumerate(row):
            row_list[col_num] += col
    return(row_list)


def create_positive_search_grid(input:List[str],
                                input_rows:List[str],
                                min_max_indexes:Dict[str,int],
                                search_length:int,
                                index:List[int])->list:

    row = index[0]
    col = index[1]
    right_searchable = True if col + search_length <= min_max_indexes['width'] else False
    down_searchable  = True if row + search_length <= min_max_indexes['length'] else False
    left_searchable  = True if col + 1 >= search_length else False

    search_strings = []
    if right_searchable:
        search_strings.append(input[row][col: col + search_length])

    if down_searchable:
        search_strings.append(input_rows[col][row: row + search_length])

    if right_searchable and down_searchable:
        diag_str = ''.join([ input[row + i][col + i] for i in range(search_length) ])
        search_strings.append(diag_str)

    if left_searchable and down_searchable:
        diag_str = ''.join([ input[row + i][col - i] for i in range(search_length) ])
        search_strings.append(diag_str)

    return(search_strings)


def create_negative_search_grid(input:List[str],
                                input_rows:List[str],
                                min_max_indexes:Dict[str,int],
                                search_length:int,
                                index:List[int])->list:

    row = index[0]
    col = index[1]
    left_searchable  = True if col + 1  >= search_length else False
    up_searchable    = True if row + 1  >= search_length else False
    right_searchable = True if col + search_length <= min_max_indexes['width'] else False

    search_strings = []
    if left_searchable:
        search_strings.append(input[row][col - search_length + 1 : col + 1 ][::-1])

    if up_searchable:
        search_strings.append(input_rows[col][row - search_length + 1 : row + 1 ][::-1])

    if left_searchable and up_searchable:
        diag_str = ''.join([ input[row - i][col - i] for i in range(search_length) ])
        search_strings.append(diag_str)

    if right_searchable and up_searchable:
        diag_str = ''.join([ input[row - i][col + i] for i in range(search_length) ])
        search_strings.append(diag_str)

    return(search_strings)


def main():

    file = '2024/day4/input.txt'
    SEARCH_TERM = 'XMAS'
    SEARCH_LENGTH = len(SEARCH_TERM)
    input = read_input(file=file)
    min_max_indexes:Dict[str,int] = {'width':len(input[0]), 'length':len(input)}
    input_rows = create_row_list(input=input, min_max_indexes=min_max_indexes)

    solution = 0
    for row_num, row in enumerate(input):
        for col_num, _ in enumerate(row):
            index = [row_num, col_num]

            search_strings = create_positive_search_grid(input=input,
                                                         input_rows=input_rows,
                                                         min_max_indexes=min_max_indexes,
                                                         search_length=SEARCH_LENGTH,
                                                         index=index)

            search_strings.extend(create_negative_search_grid(input=input,
                                                              input_rows=input_rows,
                                                              min_max_indexes=min_max_indexes,
                                                              search_length=SEARCH_LENGTH,
                                                              index=index))

            for string in search_strings:
                if string == SEARCH_TERM:
                    solution += 1
    print(solution)


if __name__ == '__main__':
    main()
