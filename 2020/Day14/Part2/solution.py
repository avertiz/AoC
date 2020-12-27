# --- Part Two ---
# For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

# A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. 
# Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
# If the bitmask bit is X, the corresponding memory address bit is floating.
# A floating bit is not connected to anything and instead fluctuates unpredictably. 
# In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

# For example, consider the following program:

# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# When this program goes to write to memory address 42, it first applies the bitmask:

# address: 000000000000000000000000000000101010  (decimal 42)
# mask:    000000000000000000000000000000X1001X
# result:  000000000000000000000000000000X1101X
# After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. 
# Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# 000000000000000000000000000000111010  (decimal 58)
# 000000000000000000000000000000111011  (decimal 59)
# Next, the program is about to write to memory address 26 with a different bitmask:

# address: 000000000000000000000000000000011010  (decimal 26)
# mask:    00000000000000000000000000000000X0XX
# result:  00000000000000000000000000000001X0XX
# This results in an address with three floating bits, causing writes to eight memory addresses:

# 000000000000000000000000000000010000  (decimal 16)
# 000000000000000000000000000000010001  (decimal 17)
# 000000000000000000000000000000010010  (decimal 18)
# 000000000000000000000000000000010011  (decimal 19)
# 000000000000000000000000000000011000  (decimal 24)
# 000000000000000000000000000000011001  (decimal 25)
# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. 
# In this example, the sum is 208.

# Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?

import pandas as pd
import numpy as np

def parse_program(row):
    if row[:4] == 'mask':
        return('mask')
    else:
        return('mem')

def define_mask(row):
    mask_dict = {}
    mask = row[-36:]
    for char in range(len(mask)):
        if mask[char] != '0':
            mask_dict[char] = mask[char]
    return(mask_dict)

def get_memory_address(row):
    row = row.split(' = ')
    memory_address = int(row[0][row[0].find("[")+1:row[0].find("]")])
    return(memory_address)

def get_decimal(row):
    row = row.split(' = ')
    decimal = int(row[1])
    return(decimal)

def convert_to_binary(decimal):
    binary = '{0:08b}'.format(decimal)
    while len(binary) < 36:
        binary = '0' + binary
    return(binary)

def apply_mask(binary, mask):
    binary_list = list(binary)
    for key in mask.keys():
        binary_list[key] = mask[key]
    masked_address = ''.join(binary_list)
    return(masked_address)

def create_address(masked_address_list):
    for char in range(len(masked_address_list)):
        if masked_address_list[char] == 'X':
            choice = np.random.choice(['0', '1'], 1, replace = True) # ...I know....not the best way
            choice = ''.join(choice)
            masked_address_list[char] = choice
    address = ''.join(masked_address_list)
    return(address)

def generate_memory_addresses(masked_address):    
    masked_address_list = list(masked_address)
    float_count = masked_address_list.count('X')
    permutations = 2 ** float_count
    memory_addresses = []
    i = 0
    while i < permutations:
        masked_address_list = list(masked_address)
        address = create_address(masked_address_list = masked_address_list)
        if address not in memory_addresses:
            memory_addresses.append(address)
            i += 1        
    return(memory_addresses)

def convert_to_decimal(binary):
    decimal = int(binary, 2)
    return(decimal)

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    memory = {}
    decimal_sum = 0
    for key, row in input.iterrows():
        if parse_program(row = row['initialization_program']) == 'mask':
            mask = define_mask(row = row['initialization_program'])
        else:
            decimal = get_decimal(row = row['initialization_program'])
            memory_address = get_memory_address(row = row['initialization_program'])            
            binary_memory_address = convert_to_binary(decimal = memory_address)
            masked_address = apply_mask(binary = binary_memory_address, mask = mask)
            memory_addresses = generate_memory_addresses(masked_address = masked_address)
            for address in memory_addresses:
                address_decimal = convert_to_decimal(binary = address)
                memory[address_decimal] = decimal
    for address in memory.keys():
        decimal_sum += memory[address]
    print(decimal_sum)

if __name__ == "__main__":
    main()