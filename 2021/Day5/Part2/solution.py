# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

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

    def mark_grid_diagonal(self, line):
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        # create points in line
        points = []
        if x1 < x2:
            x_points = [x for x in range(x1, x2 + 1)]
        else:
            x_points = [x for x in range(x1, x2 - 1, -1)]

        if y1 < y2:
            y_points = [y for y in range(y1, y2 + 1)]
        else:
            y_points = [y for y in range(y1, y2 - 1, -1)]
        
        for i, x in enumerate(x_points):
            points.append( [x, y_points[i]] )
        
        # mark grid with points:
        for point in points:
            x = point[0]
            y = point[1]
            if self.grid[y][x] == '.':
                self.grid[y][x] = 1
            else:
                self.grid[y][x] += 1


    def mark_grid_horizontal_vertical(self, line):
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
            data.mark_grid_horizontal_vertical(line=line)
        else:
            data.mark_grid_diagonal(line=line)
    data.count_dangerous_points()
    print(data.solution)

if __name__ == '__main__':
    main()