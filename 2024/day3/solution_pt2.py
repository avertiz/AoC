import re
from solution_pt1 import read_input, clean_matches

def main():
    file = '2024/day3/input.txt'
    input = read_input(file=file)

    anti_pattern = r"don't\(\).*?do\(\)"
    anti_matches = re.findall(pattern=anti_pattern, string=input)
    cleaned_input = input
    for match in anti_matches:
        cleaned_input = cleaned_input.replace(match, '')

    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern=pattern, string=cleaned_input)
    cleaned_matches = clean_matches(matches=matches)
    solution = [ x[0] * x[1] for x in cleaned_matches]
    print(sum(solution))


if __name__ == '__main__':
    main()
