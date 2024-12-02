from solution_pt1 import read_input, parse_lines

def calc_similarity(row1:list, row2:list)->list:
    similarity_list = [x * row2.count(x) for x in row1]
    return(similarity_list)


def main():
    file = '2024/day1/input.txt'
    input = read_input(file=file)
    rows = parse_lines(input=input)
    row1 = rows[0]
    row2 = rows[1]
    similarity = calc_similarity(row1=row1, row2=row2)
    print(sum(similarity))

if __name__ == '__main__':
    main()
