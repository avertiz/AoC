# --- Part Two ---
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

# byr valid:   2002
# byr invalid: 2003

# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190

# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc

# ecl valid:   brn
# ecl invalid: wat

# pid valid:   000000001
# pid invalid: 0123456789
# Here are some invalid passports:

# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# Here are some valid passports:

# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?

import pandas as pd
import string

def get_passport(df, row_num):
    passport = {}    
    while pd.notna(df['passport'].iloc[row_num]):
        row_fields = df['passport'].iloc[row_num].split(" ")
        for field in row_fields:
            key_pair = field.split(":")
            passport[key_pair[0]] = key_pair[1]
        row_num += 1
        if row_num == df.shape[0] - 1: # had to do this to account for last row
            row_fields = df['passport'].iloc[row_num].split(" ")
            for field in row_fields:
                key_pair = field.split(":")
                passport[key_pair[0]] = key_pair[1]
            values = {'passport':passport, 'row_num':row_num}
            return(values)
    row_num += 1
    values = {'passport':passport, 'row_num':row_num}
    return(values)

def valid_byr(byr):
    if len(byr) == 4 and (1920 <= int(byr) <= 2002):
        return(True)
    else:
        return(False)

def valid_iyr(iyr):
    if len(iyr) == 4 and (2010 <= int(iyr) <= 2020):
        return(True)
    else:
        return(False)

def valid_eyr(eyr):
    if len(eyr) == 4 and (2020 <= int(eyr) <= 2030):
        return(True)
    else:
        return(False)

def valid_hgt(hgt):
    numbers = []
    for number in hgt:
        if number.isdigit():
            numbers.append(number)
    numbers = "".join(numbers)
    numbers = int(numbers)
    unit = hgt[-2:]    
    if unit == 'cm' and (150 <= numbers <= 193):
        return(True)
    elif unit == 'in' and (59 <= numbers <= 76):
        return(True)
    else:
        return(False)

def valid_hcl(hcl):
    valid_chars = list(string.ascii_lowercase)[0:6]
    for number in range(0, 10):
        valid_chars.append(str(number))
    if hcl[0] != '#':
        return(False)
    for char in hcl[1:]:
        if char not in valid_chars or len(hcl[1:]) != 6:
            return(False)
    return(True)

def valid_ecl(ecl):
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl not in ecls:
        return(False)
    else:
        return(True)

def valid_pid(pid):
    numbers = []
    for number in pid.split():
        if number.isdigit():
            numbers.append(number)
    numbers = "".join(numbers)
    if len(numbers) != 9:
        return(False)
    else:
        return(True)

def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = passport.keys()    
    for rf in required_fields:
        if rf not in fields:
            return(False)
    if not valid_byr(byr = passport['byr']) or \
        not valid_iyr(iyr = passport['iyr']) or \
            not valid_eyr(eyr = passport['eyr']) or \
                not valid_hgt(hgt = passport['hgt']) or \
                    not valid_hcl(hcl = passport['hcl']) or \
                        not valid_ecl(ecl = passport['ecl']) or \
                            not valid_pid(pid = passport['pid']):
        return(False)
    return(True)
    
def scan_passports(df):
    rows = df.shape[0] - 1
    row_num = 0
    valid_passports = 0
    while rows:       
        rows = df.shape[0] - 1
        values = get_passport(df = df, row_num = row_num)        
        row_num = values['row_num']
        passport = values['passport']
        if validate_passport(passport = passport):   
            valid_passports += 1
        rows -= row_num
    return(valid_passports)        

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    valid_passports = scan_passports(df = input)
    print(valid_passports)

if __name__ == "__main__":
    main()