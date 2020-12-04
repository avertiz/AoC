# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. 
# While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. 
# Passports are separated by blank lines.

# Here is an example batch file containing four passports:

# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! 
# Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

# According to the above rules, your improved system would report 2 valid passports.

# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

import pandas as pd

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

def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = passport.keys()
    for rf in required_fields:
        if rf not in fields:
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