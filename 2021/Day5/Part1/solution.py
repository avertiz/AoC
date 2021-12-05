# Advent of Code[About][Events][Shop][Settings][Log Out]Andre Vertiz 8*
#         //2021[Calendar][AoC++][Sponsors][Leaderboard][Stats]
# Our sponsors help make Advent of Code possible:
# Assured AB - Assured pentestar allt från chip till skepp, bitar till bilar. Vi har troligtvis Sveriges mest intressanta uppdrag! Your career, Assured.
# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. 
# These line segments include the points at both ends. In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. 
# The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. 
# In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

class Solution:

    def __init__(self):
        self.file = 'input.txt'
        self.lines = []
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.grid = []
        self.solution = 0

    def parse_file(self):
        with open(self.file, 'r') as f:
            for line in f:
                line = line.rstrip()
                line = list(line.split(" -> "))
                x1y1 = list(line[0].split(','))
                x1y1 = [int(i) for i in x1y1]
                x2y2 = list(line[1].split(','))
                x2y2 = [int(i) for i in x2y2]
                self.lines.append( [x1y1, x2y2] )

    @staticmethod
    def check_if_horizontal_vertical(line):
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            return(True)
        return(False)

    def get_area(self):
        for line in self.lines:

            if self.max_x < line[0][0]:
                self.max_x = line[0][0]
            if self.max_x < line[1][0]:
                self.max_x = line[1][0]

            if self.max_y < line[0][1]:
                self.max_y = line[0][1]
            if self.max_y < line[1][1]:
                self.max_y = line[1][1]

    def create_grid(self):
        self.grid = [['.'] * (self.max_x + 1) for _ in range(self.max_y + 1)]

    def mark_grid(self, line):
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        # create points in line
        points = []
        if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for y in range(min_y, max_y + 1):
                points.append( [x1, y] )
        elif y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for x in range(min_x, max_x + 1):
                points.append( [x, y1] )

        # mark grid with points:
        for point in points:
            x = point[0]
            y = point[1]
            if self.grid[y][x] == '.':
                self.grid[y][x] = 1
            else:
                self.grid[y][x] += 1

    def count_dangerous_points(self):
        for i, row in enumerate(self.grid):
            for j, _ in enumerate(row):                
                if self.grid[i][j] == '.':
                    pass
                elif self.grid[i][j] >= 2:
                    self.solution += 1

def main():
    data = Solution()
    data.parse_file()
    data.get_area()
    data.create_grid()
    for line in data.lines:
        if data.check_if_horizontal_vertical(line=line):
            data.mark_grid(line=line)
    data.count_dangerous_points()
    print(data.solution)

if __name__ == '__main__':
    main()