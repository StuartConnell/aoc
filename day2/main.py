from typing import List


def get_inputs() -> List[List[int]]:
    lines = []
    with open("data.txt") as f:
        lines = f.readlines()
    
    inputs = []
    for line in lines:
        abc = list([int(i) for i in line.split(" ")])
        inputs.append(abc)

    return inputs

def is_ascending_valid(inputs: List[int], can_remove_item: bool = True) -> bool:

    i = 0
    j = 1
    
    while j < len(inputs):
        if inputs[i] >= inputs[j]:
            if can_remove_item: 
                l1 = inputs[:i] + inputs[i+1:]
                l2 = inputs[:j] + inputs[j+1:]

                if is_ascending_valid(l1, False):
                    return True
                return is_ascending_valid(l2, False)
            return False

        diff = inputs[j] - inputs[i]
        if not (0 < diff <= 3):
            
            if can_remove_item: 
                l1 = inputs[:i] + inputs[i+1:]
                l2 = inputs[:j] + inputs[j+1:]

                if is_ascending_valid(l1, False):
                    return True
                return is_ascending_valid(l2, False)

            return False

        j += 1
        i += 1
    return True


def is_descending_valid(inputs: List[int], can_remove_item: bool = True) -> bool:
    i = 0
    j = 1

    while j < len(inputs):
        if inputs[j] >= inputs[i]:
           
            if can_remove_item: 
                l1 = inputs[:i] + inputs[i+1:]
                l2 = inputs[:j] + inputs[j+1:]

                if is_descending_valid(l1, False):
                    return True
                return is_descending_valid(l2, False)

            return False

        diff = inputs[i] - inputs[j]
        if not (0 < diff <= 3):
          
            if can_remove_item: 
                l1 = inputs[:i] + inputs[i+1:]
                l2 = inputs[:j] + inputs[j+1:]

                if is_descending_valid(l1, False):
                    return True
                return is_descending_valid(l2, False)
            return False

        j += 1
        i += 1
    return True


def is_valid(inputs: List[int]) -> bool:
    
    asc_ok = is_ascending_valid(inputs)
    desc_ok = is_descending_valid(inputs)
    return asc_ok or desc_ok


def main() -> None:
    inputs = get_inputs()
    valid_count = 0
    for abc in inputs:
        if is_valid(abc):
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()
