# Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

# In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.
# Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

# Now, the above example does something different:

# forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
# down 5 adds 5 to your aim, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
# up 3 decreases your aim by 3, resulting in a value of 2.
# down 8 adds 8 to your aim, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
# After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

# Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

import pandas as pd

class Solution:

    def __init__(self):
        self.input = pd.read_csv('input.csv')
        self.direction_dict = {'up': [-1,0], 'forward': [0,1], 'down': [1,0]}
        self.position = [0,0]
        self.aim = 0 # adding aim
        self.solution = 0

    @staticmethod
    def parse_row(row):
        direction_and_distance = row.split(' ')
        direction_and_distance[1] = int(direction_and_distance[1])
        return(direction_and_distance)

    def update_aim(self, direction_and_distance):
        direction = direction_and_distance[0]
        distance = direction_and_distance[1]
        if direction != 'forward':
            self.aim += self.direction_dict[direction][0] * distance

    def move_sub(self, direction_and_distance):
        direction = direction_and_distance[0]
        distance = direction_and_distance[1]
        if direction == 'forward':
            self.position[0] += distance
            self.position[1] += (distance * self.aim)

    def multiply_position(self):
        self.solution = self.position[0] * self.position[1]

def main():
    data = Solution()
    for _, row in data.input.iterrows():
        direction_and_distance = data.parse_row(row = row['data'])
        data.update_aim(direction_and_distance = direction_and_distance)
        data.move_sub(direction_and_distance = direction_and_distance)
    data.multiply_position()
    print(data.solution)

if __name__ == '__main__':
    main()