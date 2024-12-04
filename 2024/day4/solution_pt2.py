from typing import Dict, List
from solution_pt1 import read_input, create_row_list


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
    if left_searchable and up_searchable:
        diag_str = ''.join([ input[row - i][col - i] for i in range(search_length) ])
        search_strings.append(diag_str)

    if right_searchable and up_searchable:
        diag_str = ''.join([ input[row - i][col + i] for i in range(search_length) ])
        search_strings.append(diag_str)

    return(search_strings)


def main():

    file = '2024/day4/input.txt'
    SEARCH_TERM = 'MAS'
    SEARCH_LENGTH = 2
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
            
            if len(search_strings) == 4:
                match_ = 0
                if search_strings[2][-1] + search_strings[0] == SEARCH_TERM:
                    match_ +=1
                if search_strings[3][-1] + search_strings[1] == SEARCH_TERM:
                     match_ +=1
                if search_strings[0][-1] + search_strings[2] == SEARCH_TERM:
                     match_ +=1
                if search_strings[1][-1] + search_strings[3] == SEARCH_TERM:
                     match_ +=1
                if match_ == 2:
                    solution += 1

    print(solution)

if __name__ == '__main__':
    main()
