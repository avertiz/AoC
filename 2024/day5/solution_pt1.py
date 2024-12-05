def read_input(file:str)->str:
    with open(file=file, mode='r') as f:
        lines = f.readlines()
    input = [x.strip() for x in lines]
    return(input)


def parse_input(input:list, split_char:str)->list:
    order = [ x.split(split_char) for x in input if split_char in x ]
    order = [ [ int(y) for y in x ] for x in order ]
    return(order)


def create_order(rules:list)->dict:
    index = {}
    for rule in rules:
        r1 = rule[0]
        r2 = rule[1]

        if r2 in index.keys():
            index[r2].append(r1)
        else:
            index[r2] = [r1]

    return(index)


def check_order(update:list, indexed_rules:dict)->bool:
    # index the order first so its easy to check positions
    # of other values without having to do another loop 
    update_index = {value:index for index, value in enumerate(update)}

    for index, value in enumerate(update): # enumerate through the update

        if indexed_rules.get(value): # Check if the value has a rule associated with it
            prior_updates_needed = indexed_rules.get(value) # get the updates that need to happen before this value can be updated

            for prior_update in prior_updates_needed: # Check each value associated with this rule
                # if the current index is less than the index of the value of the rule we are checking, thats bad
                if update_index.get(prior_update):
                    if index < update_index.get(prior_update):
                        return(False)

    return(True)


def main():
    file = '2024/day5/input.txt'
    input = read_input(file=file)
    rules = parse_input(input=input, split_char='|')
    updates = parse_input(input=input, split_char=',')
    indexed_rules = create_order(rules=rules)

    middle_values = []
    for update in updates:    
        if check_order(update=update, indexed_rules=indexed_rules):
            middle_values.append( update[ int((len(update) - 1) / 2) ] )

    print( sum(middle_values) )


if __name__ == '__main__':
    main()
