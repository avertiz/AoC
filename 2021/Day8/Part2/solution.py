# Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# So, the unique signal patterns would correspond to the following digits:

# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1
# Then, the four digits of the output value can be decoded:

# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3
# Therefore, the output value for this entry is 5353.

# Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315
# Adding all of the output values in this larger example produces 61229.

# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

import copy

class Solution:

    def __init__(self):
        self.input = 'input.txt'
        self.patterns = []
        self.outputs = []
        self.output_values = []
        self.solution = 0

    def parse_file(self):
        with open(self.input, 'r') as f:
            for line in f:
                line = line.rstrip()
                line = list(line.split(" | "))
                pattern = list(line[0].split(' '))
                output = list(line[1].split(' '))
                self.patterns.append(pattern)
                self.outputs.append(output)

    @staticmethod
    def define_configuration(pattern):
        chars = ['a','b','c','d','e','f','g']
        configuration = {0:[], 2:[], 3:[], 5:[], 6:[], 9:[]}
        known_segments = {}

        for digit_str in pattern:
            if len(digit_str) == 2:
                known_segments['one'] = [digit_str[0], digit_str[1]]
            elif len(digit_str) == 4:
                known_segments['four'] = [digit_str[0], digit_str[1], digit_str[2], digit_str[3]]
            elif len(digit_str) == 3:
                known_segments['seven'] = [digit_str[0], digit_str[1], digit_str[2]]
            elif len(digit_str) == 7:
                known_segments['eight'] = [digit_str[0], digit_str[1], digit_str[2], digit_str[3], digit_str[4], digit_str[5], digit_str[6]]                

        # populate right side for digits with all of right side segments activated using 1
        right_side = [char for char in known_segments['one']]

        for char in right_side:
            if char not in configuration[0]:
                configuration[0].append(char)
            if char not in configuration[3]:
                configuration[3].append(char)
            if char not in configuration[9]:
                configuration[9].append(char)

        # populate middle left corner using the 4 and what it has that is not in the 1
        middle_left_corner = [char for char in known_segments['four'] if char not in right_side]

        for char in middle_left_corner:
            if char not in configuration[5]:
                configuration[5].append(char)
            if char not in configuration[6]:                
                configuration[6].append(char)
            if char not in configuration[9]:
                configuration[9].append(char)
        
        # populate top using 7 and what is not in 1
        top = [char for char in known_segments['seven'] if char not in right_side]

        for char in top:
            if char not in configuration[0]:
                configuration[0].append(char)
            if char not in configuration[2]:
                configuration[2].append(char)
            if char not in configuration[3]:
                configuration[3].append(char)
            if char not in configuration[5]:
                configuration[5].append(char)
            if char not in configuration[6]:
                configuration[6].append(char)
            if char not in configuration[9]:
                configuration[9].append(char)
        
        # more deduction based on what is now populated 
        bottom_left_corner = [char for char in chars if char not in configuration[9]]

        for char in bottom_left_corner:
            if char not in configuration[0]:
                configuration[0].append(char)
            if char not in configuration[2]:
                configuration[2].append(char)
            if char not in configuration[6]:
                configuration[6].append(char)
                
        # now there are a bunch of single segments we need to figure out and populate where necessary 
        middle_left_corner_set = set(middle_left_corner)

        for digit_str in pattern:            
            if len(digit_str) == 5:
                digit_set = set(digit_str)
                if middle_left_corner_set.issubset(digit_set):
                    five = digit_str

        for char in five:
            if char not in configuration[5]:
                configuration[5].append(char) # done with 5

        bottom_left_corner_set = set(bottom_left_corner)

        for digit_str in pattern:            
            if len(digit_str) == 5:
                digit_set = set(digit_str)
                if bottom_left_corner_set.issubset(digit_set):
                    two = digit_str

        for char in two:
            if char not in configuration[2]:
                configuration[2].append(char) # done with 2
        
        bottom = [char for char in five if char not in top and char not in middle_left_corner and char not in right_side]

        for char in bottom:
            if char not in configuration[3]:
                configuration[3].append(char)
            if char not in configuration[9]:
                configuration[9].append(char) # done with 9

        middle = [char for char in configuration[2] if char not in configuration[3] and char not in bottom_left_corner_set]

        for char in middle:
            if char not in configuration[3]:
                configuration[3].append(char) # done with 3

        top_left = [char for char in configuration[5] if char not in configuration[3]]
        
        for char in top_left:
            if char not in configuration[0]:
                configuration[0].append(char) # done with 0

        bottom_right = [char for char in configuration[5] if char not in configuration[6]]

        for char in bottom_right:
            if char not in configuration[6]:
                configuration[6].append(char) # done with 6
                
        return(configuration)

    def classify_digit(self, digit_str, configuration):
        if len(digit_str) == 2:
            return(1)
        elif len(digit_str) == 4:
            return(4)
        elif len(digit_str) == 3:
            return(7)
        elif len(digit_str) == 7:
            return(8)
        else:
            digit_str_list = [char for char in digit_str] # convert characters to list
            for digit, chars in configuration.items():
                temp_digit = copy.deepcopy(digit)
                for char in digit_str_list:
                    if char not in chars or len(digit_str_list) != len(chars):
                        temp_digit = None
                        break
                if temp_digit or str(temp_digit) == '0':
                    return(temp_digit)
    
    @staticmethod
    def digits_to_output_value(output_value_list):
        output_value_list = [str(integer) for integer in output_value_list]
        output_value = "". join(output_value_list)
        output_value = int(output_value)
        return(output_value)

def main():
    data = Solution()
    data.parse_file()
    for index, output in enumerate(data.outputs):
        configuration = data.define_configuration(pattern = data.patterns[index])
        output_value_list = []
        for digit_str in output:             
            digit = data.classify_digit(digit_str=digit_str, configuration=configuration)
            output_value_list.append(digit)
        output_value = data.digits_to_output_value(output_value_list=output_value_list)
        data.output_values.append(output_value)
    data.solution = sum(data.output_values) 
    print(data.solution)

if __name__ == '__main__':
    main()