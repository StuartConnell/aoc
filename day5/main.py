from typing import Tuple, List,  Dict

type Rule = Dict[int, int]

def get_inputs() -> Tuple[List[Rule], List[List[int]]]:

    with open("example.txt") as f:
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
            rule = Rule(first=int(splits[0]), second=int(splits[1]))
            rules.append(rule)
        else:
            splits = line.split(',')
            cast_splits = [int(s) for s in splits]
            updates.append(cast_splits)

    return rules, updates


def valid_updates(rules: List[Rule], updates: List[List[int]]):

    for update in updates:
        for num in update:



def main():
    rules, updates = get_inputs()


if __name__ == '__main__':
    main()
