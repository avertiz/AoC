# --- Day 7: Handy Haversacks ---
# You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: 
# all flights are currently delayed due to issues in luggage processing.

# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; 
# bags must be color-coded and must contain specific quantities of other color-coded bags. 
# Apparently, nobody responsible for these regulations considered how long they would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. 
# In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? 
# (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

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
        words = condition.split(" ")
        sub_rule = str(words[1] + " " + words[2])
        sub_rules.append(sub_rule)
    return(sub_rules)

def get_sub_conditions(rules, current_rule):
    condition_list = rules[current_rule]
    sub_rules = get_sub_rules(rules = rules, current_rule = current_rule)
    sub_rules_tracking = ['other bags.']
    while sub_rules:
        for sr in sub_rules:
            if sr not in sub_rules_tracking:
                sub_rules_tracking.append(sr)
                condition_list += rules[sr]
                current_sub_rules = get_sub_rules(rules = rules, current_rule = sr)
                for csr in current_sub_rules:
                    if csr not in sub_rules:
                        sub_rules.append(csr)                
                sub_rules.remove(sr)
            else:
                sub_rules.remove(sr)
    return(condition_list)

def valid_rule(condition_list, my_condition):
    if any(my_condition in s for s in condition_list):
        return(True)
    else:
        return(False)

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    gold_bag_rules = 0
    rules = get_rules(df = input)
    for rule in rules.keys():
        condition_list = get_sub_conditions(rules = rules, current_rule = rule)
        if valid_rule(condition_list = condition_list, my_condition = 'shiny gold'):
            gold_bag_rules += 1
    print(gold_bag_rules)

if __name__ == "__main__":
    main()