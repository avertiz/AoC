# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

# So, the gamma rate is the binary number 10110, or 22 in decimal.

# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

import pandas as pd

class Solution:

    def __init__(self):
        self.input = pd.read_csv('input.csv', dtype=str)
        self.gamma_rate = []
        self.gamma_rate_binary = None
        self.epsilon_rate = []        
        self.epsilon_rate_binary = None
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

    def update_gamma_rate(self):
        for value_list in self.bit_count_dict.values():
            most_common = max(value_list)
            most_common_index = value_list.index(most_common)
            self.gamma_rate.append(most_common_index)

    def update_epsilon_rate(self):
        for value_list in self.bit_count_dict.values():
            least_common = min(value_list)
            least_common_index = value_list.index(least_common)
            self.epsilon_rate.append(least_common_index)

    @staticmethod
    def create_binary_num(binary_list):
        binary_list = [str(i) for i in binary_list]
        binary_string = ''.join(binary_list)
        binary_num = int(binary_string, 2)
        return(binary_num)

def main():
    data = Solution()
    for _, row in data.input.iterrows():
        data.tally_bits(num = row['data'])
    data.update_gamma_rate()
    data.update_epsilon_rate()
    data.gamma_rate_binary = data.create_binary_num(binary_list = data.gamma_rate)
    data.epsilon_rate_binary = data.create_binary_num(binary_list = data.epsilon_rate)
    data.solution = data.gamma_rate_binary * data.epsilon_rate_binary
    print(data.solution)

if __name__ == '__main__':
    main()