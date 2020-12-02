# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! 
# The Official Toboggan Corporate Policy actually works a little differently.

# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; 
# Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

import pandas as pd

def valid_password(pos1, pos2, letter, password):
    hits = 0
    if password[pos1-1] == letter:
        hits += 1
    if password[pos2-1] == letter:
        hits += 1
    if hits == 1:
        return(True)
    else:
        return(False)

def get_inputs(policy):
    string = policy[:len(policy) - 2]
    numbers = string.split("-")
    pos1 = int(numbers[0])
    pos2 = int(numbers[1])
    letter = policy[len(policy)-1:]
    dict_ = {'pos1':pos1, 'pos2':pos2, 'letter':letter}
    return(dict_)

def main():
    input = pd.read_csv('input.csv')
    count = 0
    for index, row in input.iterrows():
        inputs = get_inputs(policy = row['policy'])
        if valid_password(pos1 = inputs['pos1'], pos2 = inputs['pos2'], letter = inputs['letter'], password = row['password']):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
