# --- Part Two ---
# It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

# Consider again your shiny gold bag and the rules from the above example:

# faded blue bags contain 0 other bags.
# dotted black bags contain 0 other bags.
# vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
# dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

# Of course, the actual rules have a small chance of going several levels deeper than this example; 
# be sure to count all of the bags, even if the nesting becomes topologically impractical!

# Here's another example:

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# In this example, a single shiny gold bag must contain 126 other bags.

# How many individual bags are required inside your single shiny gold bag?

import pandas as pd
import copy

def get_rules(df):
    rules = {}
    for key, row in df.iterrows():
        rule = row['rule'].split(' bags contain ')[0]
        conditions = row['rule'].split(' bags contain ')[1]
        conditions = conditions.split(',')
        condition_list = []
        for condition in conditions:
            condition_list.append(condition.strip())
        rules[rule] = condition_list
    return(rules)

def get_sub_rules(rules, current_rule):
    sub_rules = []
    condition_list = rules[current_rule]
    for condition in condition_list:
        if condition != 'no other bags.':
            words = condition.split(" ")
            sub_rule = {str(words[1] + " " + words[2]):int(words[0])}
            sub_rules.append(sub_rule)
    return(sub_rules)

def bag_multiplyer(rules, current_rule, multiplier):
    sub_rules = get_sub_rules(rules = rules, current_rule = current_rule)
    if not sub_rules: 
        return(0)
    else:
        sums = []
        for sr in sub_rules:  
            current_rule = list(sr.keys())[0]
            new_multiplier = list(sr.values())[0]
            sum_path = new_multiplier + new_multiplier * bag_multiplyer(rules = rules, current_rule = current_rule, multiplier = new_multiplier)
            sums.append(sum_path)
        sums = sum(sums)
        return(sums)
            
def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    rules = get_rules(df = input)
    bag_sum = bag_multiplyer(rules = rules, current_rule = 'shiny gold', multiplier = 0)
    print(bag_sum)

if __name__ == "__main__":
    main()