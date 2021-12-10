# Next, you need to find the largest basins so you know what areas are most important to avoid.

# A basin is all locations that eventually flow downward to a single low point. 
# Therefore, every low point has a basin, although some basins are very small. 
# Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

# The top-left basin, size 3:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The top-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The middle basin, size 14:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The bottom-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

# What do you get if you multiply together the sizes of the three largest basins?

class Solution:

    def __init__(self):
        self.input = 'input.txt'
        self.heights = []
        self.row_len = 0
        self.col_len = 0
        self.heights_checked = []
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

    def get_neighbors(self, row, col):
        neighbors = {}
        try:
            # right
            neighbors['right'] = [self.heights[row][col + 1] , row, col + 1]
        except IndexError:
            pass

        try:
            # bottom
            neighbors['bottom'] = [self.heights[row + 1][col], row + 1, col]
        except IndexError:
            pass

        try:
            # left
            if col - 1 >= 0:
                neighbors['left'] = [self.heights[row][col - 1], row, col - 1]
        except IndexError:
            pass

        try:
            # top
            if row - 1 >= 0:
                neighbors['top'] = [self.heights[row - 1][col], row - 1, col]
        except IndexError:
            pass

        return(neighbors)

    def count_basin(self, neighbors, low_point, count):
        for neighbor in neighbors.values():
            num = neighbor[0]
            row = neighbor[1]
            col = neighbor[2]
            # base case
            if num == 9 or num <= low_point or [row, col] in self.heights_checked:
                pass
            # recurse
            else:
                self.heights_checked.append( [row, col] )
                neighbors_of_neighbor = self.get_neighbors(row=row, col=col)
                temp = self.count_basin(neighbors=neighbors_of_neighbor, low_point=num, count = 0)
                count += 1 + temp
        return(count)

def main():
    data = Solution()
    data.parse_file()
    basins = []
    for i, row in enumerate(data.heights):
        for j, num in enumerate(row):
            if data.low_point_check(num=num, row=i, col=j):
                data.heights_checked.append([i,j])
                neighbors = data.get_neighbors(row=i, col=j)
                basin = data.count_basin(neighbors=neighbors, low_point=num, count=1)
                basins.append(basin)   
    basins.sort(reverse=True)
    data.solution = basins[0] * basins[1] * basins[2]
    print(data.solution)

if __name__ == '__main__':
    main()