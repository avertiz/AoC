# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

import pandas as pd

def row_len_check(row, position):
    if len(row) <= position + 7:
        row *= position
        return(row)
    else:
        return(row)

def traverse(df, row_num, position, trees, slope):
    row = df['map'].iloc[row_num]
    row = row_len_check(row = row, position = position)
    if row_num == df.shape[0]-1:
        if row[position] == '#':
            trees += 1
        return(trees)
    else:
        if row[position] == '#':
            trees += 1
        return traverse(df = df, row_num = row_num + slope[0], position = position + slope[1], trees = trees, slope = slope)

def main():
    input = pd.read_csv('input.csv')
    slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]
    trees = 1
    for s in slopes:
        tree_count = traverse(df = input, row_num = 0, position = 0, trees = 0, slope = s)
        trees *= tree_count
    print(trees)

if __name__ == "__main__":
    main()