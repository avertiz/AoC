from solution_pt1 import read_input, parse_input, create_order, check_order

def reorder_update(update:list, indexed_rules:dict)->list:
    reordered_update = [] # create a new list

    while len(reordered_update) < len(update):        

        for _, value in enumerate(update):
            
            if indexed_rules.get(value):
                prior_updates_needed = indexed_rules.get(value)
                # get list of values in update that need to be processed before current value           
                intersection = [x for x in prior_updates_needed if x in update] 
                count = 0
                for i in intersection:
                    # check each one to see if they are already i nthe new list                 
                    if i not in reordered_update:
                        count = +1
                if count == 0 and value not in reordered_update:
                    # If they are all already in there, add the current value if its not already in there,
                    # else keep going.
                    reordered_update.append(value)
                else:
                    continue

            # If nothing needs to be processed before it,
            # just add it to the new list if its not already in there
            elif value not in reordered_update:
                reordered_update.append(value)
    
    return(reordered_update)


def main():
    file = '2024/day5/input.txt'
    input = read_input(file=file)
    rules = parse_input(input=input, split_char='|')
    updates = parse_input(input=input, split_char=',')
    indexed_rules = create_order(rules=rules)

    middle_values = []
    for update in updates:    
        if check_order(update=update, indexed_rules=indexed_rules):
            continue
        else:
            updated_order = reorder_update(update=update, indexed_rules=indexed_rules)
            middle_values.append( updated_order[ int((len(updated_order) - 1) / 2) ] )

    print( sum(middle_values) )


if __name__ == '__main__':
    main()
