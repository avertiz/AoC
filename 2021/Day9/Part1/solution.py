# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. 
# The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. 
# Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. 
# (Diagonal locations do not count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). 
# All other locations on the heightmap have some lower adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. 
# The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

class Solution:

    def __init__(self):
        self.input = 'input.txt'
        self.heights = []
        self.row_len = 0
        self.col_len = 0
        self.solution = 0

    def parse_file(self):
        with open(self.input, 'r') as f:
            for line in f:
                line = line.rstrip()
                line = [int(char) for char in line]
                self.heights.append(line)
        self.row_len = len(self.heights[0]) - 1
        self.col_len = len(self.heights) - 1

    def low_point_check(self, num, row, col):
        nums = [num]
        try:
            # right
            nums.append(self.heights[row][col + 1])
        except IndexError:
            pass

        try:
            # bottom
            nums.append(self.heights[row + 1][col])
        except IndexError:
            pass

        try:
            # left
            if col - 1 >= 0:
                nums.append(self.heights[row][col - 1])
        except IndexError:
            pass

        try:
            # top
            if row - 1 >= 0:
                nums.append(self.heights[row - 1][col])
        except IndexError:
            pass
        if num == min(nums) and nums.count(num) < 2:
            return(True)

        return(False)


def main():
    data = Solution()
    data.parse_file()
    risk_level = []
    for i, row in enumerate(data.heights):
        for j, num in enumerate(row):
            if data.low_point_check(num=num, row=i, col=j):
                risk_level.append(num + 1)
    data.solution = sum(risk_level)
    print(data.solution)

if __name__ == '__main__':
    main()