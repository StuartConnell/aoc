from typing import Tuple, List, Dict
from collections import defaultdict


type Rule = List[int]


def get_inputs() -> Tuple[List[Rule], List[List[int]]]:

    with open("data.txt") as f:
        lines = f.readlines()

    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.rstrip())

    rules_ended = False
    rules = []
    updates = []
    for line in stripped_lines:

        if line == '':
            rules_ended = True
            continue

        if not rules_ended:
            splits = line.split('|')
            rule: Rule = [int(splits[0]), int(splits[1])]
            rules.append(rule)
        else:
            splits = line.split(',')
            cast_splits = [int(s) for s in splits]
            updates.append(cast_splits)

    return rules, updates


def format_rules(rules: List[Rule]) -> Dict[int, List[int]]:
    
    new_rules = defaultdict(list)
    for rule in rules:
        key = rule[0]
        if rule[1] is not None:
            new_rules[key].append(rule[1])

    retval = {k: v for k, v in new_rules.items()}
    return retval
        

def valid_updates(rules: Dict[int, List[int]], updates: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
    valid = []
    invalid = []
    for update in updates:
        is_valid = True
        for num in update:
            if not is_valid:
                break
            
            rule = rules.get(num)
            if not rule:
                continue

            for r in rule:
                num_index = update.index(num)
                
                try:
                    r_index = update.index(r)
                except ValueError:
                    continue

                if num_index > r_index:
                    is_valid = False
                    break

        if is_valid:
            valid.append(update)
        else:
            invalid.append(update)
    return valid, invalid


def find_middle_values(valid_values: List[List[int]]) -> List[int]:
    middle_values = []

    for values in valid_values:
        middle_value = values[int((len(values) - 1) / 2)]
        middle_values.append(middle_value)
    return middle_values


def main():
    rules, updates = get_inputs()
    formatted_rules = format_rules(rules)
    valid, invalid = valid_updates(formatted_rules, updates)   
    middle_values = find_middle_values(valid)
    
    total = 0
    for middle_value in middle_values:
        total += middle_value
    print(total)

if __name__ == '__main__':
    main()

