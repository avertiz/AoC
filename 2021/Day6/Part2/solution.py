# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

# After 256 days in the example above, there would be a total of 26984457539 lanternfish!

# How many lanternfish would there be after 256 days?

import copy
from os import cpu_count

class Solution:

    def __init__(self):
        self.file = 'input.txt'
        # going to make a dict of counts so it's faster....
        self.fishes = {
            0:0,
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0
        }
        self.solution = 0
    
    def parse_file(self):
        with open(self.file, 'r') as f:
            for line in f:
                line = line.rstrip()                
                line = list(line.split(","))
                for i in line:
                    i = int(i)
                    self.fishes[i] += 1

    def add_day(self):
        new_fishes = copy.deepcopy(self.fishes)
        reproducers = new_fishes[0]
        for key in self.fishes.keys():            
            if key > 0:
                new_fishes[key - 1] = self.fishes[key]
        new_fishes[8] = 0
        new_fishes[6] += reproducers
        new_fishes[8] += reproducers
        self.fishes = new_fishes

def main():
    data = Solution()
    data.parse_file()
    for day in range(256):
        data.add_day()
    total = 0
    for fish in data.fishes.keys():
        total += data.fishes[fish]
    data.solution = total
    print(data.solution)

if __name__ == '__main__':
    main()