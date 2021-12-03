# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

# Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, 
# start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:

# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
# For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

# Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
# Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
# In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
# In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
# In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
# As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
# Then, to determine the CO2 scrubber rating value from the same example above:

# Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
# Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
# In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
# As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
# Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

from os import remove
import pandas as pd

class Solution:

    def __init__(self):
        self.input = pd.read_csv('input.csv', dtype=str)
        self.solution = None
        self.bit_count_dict = { # first element of value is 0 count, second element is 1 count
                                0:[0,0],
                                1:[0,0],
                                2:[0,0],
                                3:[0,0],
                                4:[0,0],
                                5:[0,0],
                                6:[0,0],
                                7:[0,0],
                                8:[0,0],
                                9:[0,0],
                               10:[0,0],
                               11:[0,0],           
                            }

    def tally_bits(self, num):
        for index, value in enumerate(num):
            if value == '0':
                self.bit_count_dict[index][0] += 1
            elif value == '1':
                self.bit_count_dict[index][1] += 1

    def reset_bit_count_dict(self):
        for key in self.bit_count_dict.keys():
            self.bit_count_dict[key] = [0,0]

    def get_oxy_gen_rating_nums(self):

        num_list = self.input['data'].tolist()
        index = 0

        while len(num_list) > 1:
            
            # find most common bits by current index
            for num in num_list:
                self.tally_bits(num = num)            
            if self.bit_count_dict[index][0] == self.bit_count_dict[index][1]:
                most_common_bit = '1'
            else:
                most_common = max(self.bit_count_dict[index])
                most_common_bit = str(self.bit_count_dict[index].index(most_common))
            
            # now remove binary numbers that do not meet bit criteria
            nums_to_remove = []
            for num in num_list:    
                if num[index] != most_common_bit:
                    nums_to_remove.append(num)

            for num in nums_to_remove:
                if len(num_list) > 1:
                    num_list.remove(num)
                else:
                    self.reset_bit_count_dict()
                    return(num_list)
            
            # reset remove list
            nums_to_remove = []
            # reset count dict
            self.reset_bit_count_dict()
            # go to next index
            index += 1

        self.reset_bit_count_dict()
        return(num_list)

    def get_co2_scrub_rating_nums(self):

        num_list = self.input['data'].tolist()
        index = 0

        while len(num_list) > 1:
            
            # find least common bits by current index
            for num in num_list:
                self.tally_bits(num = num)            
            if self.bit_count_dict[index][0] == self.bit_count_dict[index][1]:
                least_common_bit = '0'
            else:
                least_common = min(self.bit_count_dict[index])
                least_common_bit = str(self.bit_count_dict[index].index(least_common))
            
            # now remove binary numbers that do not meet bit criteria
            nums_to_remove = []
            for num in num_list:    
                if num[index] != least_common_bit:
                    nums_to_remove.append(num)

            for num in nums_to_remove:
                if len(num_list) > 1:
                    num_list.remove(num)
                else:
                    self.reset_bit_count_dict()
                    return(num_list)
            
            # reset remove list
            nums_to_remove = []
            # reset count dict
            self.reset_bit_count_dict()
            # go to next index
            index += 1

        self.reset_bit_count_dict()
        return(num_list)

    @staticmethod
    def create_binary_num(binary_list):
        binary_list = [str(i) for i in binary_list]
        binary_string = ''.join(binary_list)
        binary_num = int(binary_string, 2)
        return(binary_num)

def main():
    data = Solution()
    oxy_gen_rating_num = data.get_oxy_gen_rating_nums()
    oxy_gen_rating_num = data.create_binary_num(binary_list=oxy_gen_rating_num)
    co2_scrub_rating_num = data.get_co2_scrub_rating_nums()
    co2_scrub_rating_num = data.create_binary_num(binary_list=co2_scrub_rating_num)
    data.solution = oxy_gen_rating_num * co2_scrub_rating_num
    print(data.solution)

if __name__ == '__main__':
    main()