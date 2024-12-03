import re


def read_input(file:str)->str:
    with open(file=file, mode='r') as f:
        lines = f.readlines()
    input = [x.strip() for x in lines]
    input = ''.join(input) # [x.strip() for x in lines]
    return(input)


def clean_matches(matches:list)->list:
    cleaned_matches = []
    for match in matches:
        cleaned_match = match.replace('mul(', '').replace(')', '')
        cleaned_match = cleaned_match.split(',')
        cleaned_match = [int(x) for x in cleaned_match]
        cleaned_matches.append(cleaned_match)
    return(cleaned_matches)


def main():
    file = '2024/day3/input.txt'
    input = read_input(file=file)
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern=pattern, string=input)
    cleaned_matches = clean_matches(matches=matches)
    solution = [ x[0] * x[1] for x in cleaned_matches]
    print(sum(solution))


if __name__ == '__main__':
    main()
