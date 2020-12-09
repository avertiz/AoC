# --- Part Two ---
# The final step in breaking the XMAS encryption relies on the invalid number you just found: 
# you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

# Again consider the above example:

# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. 
# (Of course, the contiguous set of numbers in your actual list might be much longer.)

# To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

# What is the encryption weakness in your XMAS-encrypted list of numbers?

import pandas as pd

def get_preamble(df, row_num):
    preamble = []
    for row in range(row_num, row_num + 25):
        preamble.append(df['xmas'][row])
    return(preamble)

def valid_next_num(df, row_num):
    preamble = get_preamble(df = df, row_num = row_num)
    next_num = df['xmas'][row_num + 25]
    for num in range(len(preamble)):
        first_num = preamble[num]
        for num2 in range(num + 1, len(preamble)) :            
            second_num = preamble[num2]
            if first_num + second_num == next_num:
                return(True)
    return(False)

def get_contiguous_list(df, num):
    for i in range(len(df.index)):
        num_list = df['xmas'][i:].tolist()
        length = len(num_list)
        for j in range(length):
            if sum(num_list) == num:
                return(num_list)
            else:
                num_list.pop(len(num_list) - 1)
    return(None)

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    for row in range(len(input.index)):
        if not valid_next_num(df = input, row_num = row):
            num = int(input['xmas'][row + 25])
            break
    num_list = get_contiguous_list(df = input, num = num)
    answer = min(num_list) + max(num_list)
    print(answer)

if __name__ == "__main__":
    main()