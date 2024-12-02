def read_input(file:str)->list:
    with open(file=file, mode='r') as f:
        lines = f.readlines()
    input = [x.strip() for x in lines]
    return(input)

def parse_lines(input:list)->list:
    row1 = []
    row2 = []
    for line in input:
        line_split = line.split('   ')
        row1.append(int(line_split[0]))
        row2.append(int(line_split[1]))
    rows = [row1, row2]
    return(rows)

def compare_rows(row1:list, row2:list)->list:
    row1.sort()
    row2.sort()
    diffs = [ abs( row1[i] - row2[i] ) for i, _ in enumerate(row1) ]
    return(diffs)


def main():
    file = '2024/day1/input.txt'
    input = read_input(file=file)
    rows = parse_lines(input=input)
    row1 = rows[0]
    row2 = rows[1]
    diffs = compare_rows(row1=row1, row2=row2)
    print(sum(diffs))


if __name__ == '__main__':
    main()
