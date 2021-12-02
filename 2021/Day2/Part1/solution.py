# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

import pandas as pd

class Solution:

    def __init__(self):
        self.input = pd.read_csv('input.csv')
        # dict for each direction that we will use to multiply position
        # first element is up/down, second element is forward/back
        self.direction_dict = {'up': [-1,0], 'forward': [0,1], 'down': [1,0]} 
        # starting position, first element is depth and second element is horizontal
        self.position = [0,0]
        self.solution = 0

    # returns list. First element is direction and second element is distance
    @staticmethod
    def parse_row(row):
        direction_and_distance = row.split(' ')
        direction_and_distance[1] = int(direction_and_distance[1])
        return(direction_and_distance)

    def move_sub(self, direction_and_distance):
        direction = direction_and_distance[0]
        distance = direction_and_distance[1]
        up_down = self.direction_dict[direction][0] * distance
        forward_back = self.direction_dict[direction][1] * distance
        self.position[0] += up_down
        self.position[1] += forward_back

    def multiply_position(self):
        self.solution = self.position[0] * self.position[1]

def main():
    data = Solution()
    for _, row in data.input.iterrows():
        direction_and_distance = data.parse_row(row = row['data'])
        data.move_sub(direction_and_distance = direction_and_distance)
    data.multiply_position()
    print(data.solution)

if __name__ == '__main__':
    main()